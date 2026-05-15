"""Regression tests for save-the-date and save-the-date-family RSVP routes.

These prove the helper refactor (T1) preserves the existing external behavior:
same DB rows, same email subject/body, same `from` address. Covers AC-B13.
"""
import sqlite3

from tests.conftest import TEST_DB_PATH


def test_save_the_date_rsvp_inserts_rows(client):
    payload = {"guests": [
        {"name": "Klaus", "attending": True},
        {"name": "Olga", "attending": False},
    ]}
    r = client.post("/save-the-date/rsvp", json=payload)
    assert r.status_code == 200
    assert r.get_json() == {"success": True}

    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT guest_name, attending FROM rsvp ORDER BY guest_name")
    rows = cur.fetchall()
    conn.close()
    assert rows == [("Klaus", 1), ("Olga", 0)]


def test_save_the_date_family_rsvp_inserts_rows(client):
    payload = {"guests": [{"name": "Hans", "attending": True}]}
    r = client.post("/save-the-date-family/rsvp", json=payload)
    assert r.status_code == 200

    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT guest_name, attending FROM rsvp")
    rows = cur.fetchall()
    conn.close()
    assert rows == [("Hans", 1)]


def test_save_the_date_email_uses_correct_from(client, app, monkeypatch):
    captured = {}

    def fake_send(payload):
        captured.update(payload)
        return {"id": "1"}

    monkeypatch.setattr(app, "RESEND_API_KEY", "fake_key")
    monkeypatch.setattr(app.resend.Emails, "send", fake_send)

    r = client.post("/save-the-date/rsvp", json={"guests": [{"name": "X", "attending": True}]})
    assert r.status_code == 200
    assert captured["from"] == "kontakt@beas-coaching.de"
    # Subject contract preserved
    assert captured["subject"].startswith("RSVP Hochzeit - ")
    # Body header preserved
    assert "Neue RSVP-Anmeldung für die Hochzeit!" in captured["text"]
    assert "GESAMTÜBERSICHT" in captured["text"]


def test_save_the_date_family_email_uses_correct_from(client, app, monkeypatch):
    captured = {}

    def fake_send(payload):
        captured.update(payload)
        return {"id": "1"}

    monkeypatch.setattr(app, "RESEND_API_KEY", "fake_key")
    monkeypatch.setattr(app.resend.Emails, "send", fake_send)

    r = client.post(
        "/save-the-date-family/rsvp",
        json={"guests": [{"name": "Y", "attending": False}]},
    )
    assert r.status_code == 200
    assert captured["from"] == "RSVP Hochzeit <onboarding@resend.dev>"


def test_save_the_date_empty_guests_returns_400(client):
    r = client.post("/save-the-date/rsvp", json={"guests": []})
    assert r.status_code == 400


def test_save_the_date_no_data_returns_400(client):
    r = client.post("/save-the-date/rsvp", json={})
    assert r.status_code == 400


def test_save_the_date_db_and_email_share_submitted_at(client, app, monkeypatch):
    """AC-B13 regression: handler must pass the SAME submitted_at to both
    the DB row and the email body. Two separate datetime.now() calls would
    differ in microseconds and violate 'same DB rows, same values'."""
    captured = {}

    def fake_send(payload):
        captured.update(payload)
        return {"id": "1"}

    monkeypatch.setattr(app, "RESEND_API_KEY", "fake_key")
    monkeypatch.setattr(app.resend.Emails, "send", fake_send)

    r = client.post(
        "/save-the-date/rsvp",
        json={"guests": [{"name": "Z", "attending": True}]},
    )
    assert r.status_code == 200

    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT submitted_at FROM rsvp WHERE guest_name = ?", ("Z",))
    db_iso = cur.fetchone()[0]
    conn.close()

    # Email body shows DD.MM.YYYY HH:MM — must match DB timestamp formatted the same way.
    from datetime import datetime as _dt
    db_dt = _dt.fromisoformat(db_iso)
    expected_in_email = db_dt.strftime("%d.%m.%Y %H:%M")
    assert f"Datum: {expected_in_email}" in captured["text"]


def test_save_the_date_no_api_key_skips_get_all_rsvps(client, app, monkeypatch):
    """AC-B13 regression: pre-refactor code did not call get_all_rsvps when
    RESEND_API_KEY was unset. After refactor this must still hold."""
    monkeypatch.setattr(app, "RESEND_API_KEY", None)
    calls = {"n": 0}
    real = app.get_all_rsvps

    def counting():
        calls["n"] += 1
        return real()

    monkeypatch.setattr(app, "get_all_rsvps", counting)
    r = client.post(
        "/save-the-date/rsvp",
        json={"guests": [{"name": "Q", "attending": True}]},
    )
    assert r.status_code == 200
    assert calls["n"] == 0
