"""Tests for the /invitation routes, helpers, schema, and email content.

Covers: AC-B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, B14, B15, B16, B17, B18.
"""
import sqlite3
import uuid as uuid_mod

import pytest

from tests.conftest import TEST_DB_PATH


# ---------- AC-B12: init_db creates both tables ----------
def test_init_db_creates_both_tables(app):
    app.init_db()
    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = {row[0] for row in cur.fetchall()}
    conn.close()
    assert "rsvp" in tables
    assert "invitation_rsvp" in tables


# ---------- AC-B1, AC-B2: routes ----------
def test_get_invitation_returns_html(client):
    r = client.get("/invitation")
    assert r.status_code == 200
    assert b"Einladung zu" in r.data


def test_get_invitation_asset_missing_returns_404(client):
    r = client.get("/invitation/does_not_exist.png")
    assert r.status_code == 404


def test_get_invitation_image_returns_png(client):
    """AC-B2 positive case: real asset is served with correct Content-Type."""
    r = client.get("/invitation/Gemini_Generated_Image_ohq6qtohq6qtohq6.png")
    assert r.status_code == 200
    assert r.headers["Content-Type"].startswith("image/")


# ---------- AC-B3, AC-B4, AC-B5: verify ----------
def test_verify_correct_password(client):
    r = client.post("/invitation/verify", json={"password": "150826"})
    assert r.status_code == 200
    assert r.get_json() == {"success": True}


def test_verify_wrong_password(client):
    r = client.post("/invitation/verify", json={"password": "wrong"})
    assert r.status_code == 401
    assert r.get_json() == {"success": False}


def test_verify_no_body(client):
    r = client.post("/invitation/verify")
    assert r.status_code == 401


# ---------- AC-B6: rsvp happy path ----------
def test_rsvp_valid_payload_inserts_rows(client):
    payload = {"guests": [
        {"name": "Anna Müller", "diet": "Vegetarisch", "allergies": "Nüsse"},
        {"name": "Max Müller", "diet": "Ich esse alles", "allergies": ""},
    ]}
    r = client.post("/invitation/rsvp", json=payload)
    assert r.status_code == 200
    assert r.get_json() == {"success": True}

    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT guest_name, diet, allergies, submission_group FROM invitation_rsvp ORDER BY guest_name"
    )
    rows = cur.fetchall()
    conn.close()
    assert len(rows) == 2
    assert rows[0][3] == rows[1][3]  # same submission_group
    assert {r[0] for r in rows} == {"Anna Müller", "Max Müller"}


# ---------- AC-B7: empty guests ----------
def test_rsvp_empty_guests_returns_400(client):
    r = client.post("/invitation/rsvp", json={"guests": []})
    assert r.status_code == 400


# ---------- AC-B8: whitespace name ----------
def test_rsvp_whitespace_name_rejected(client):
    payload = {"guests": [{"name": "   ", "diet": "Vegan", "allergies": ""}]}
    r = client.post("/invitation/rsvp", json=payload)
    assert r.status_code == 400
    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM invitation_rsvp")
    count = cur.fetchone()[0]
    conn.close()
    assert count == 0


# ---------- AC-B9: invalid diet ----------
def test_rsvp_invalid_diet_rejected(client):
    payload = {"guests": [{"name": "Anna", "diet": "Carnivore", "allergies": ""}]}
    r = client.post("/invitation/rsvp", json=payload)
    assert r.status_code == 400
    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM invitation_rsvp")
    count = cur.fetchone()[0]
    conn.close()
    assert count == 0


# ---------- AC-B10: missing allergies stored as empty string ----------
def test_rsvp_missing_allergies_stored_as_empty(client):
    payload = {"guests": [{"name": "Eva", "diet": "Vegan"}]}
    r = client.post("/invitation/rsvp", json=payload)
    assert r.status_code == 200
    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT allergies FROM invitation_rsvp WHERE guest_name = ?", ("Eva",))
    val = cur.fetchone()[0]
    conn.close()
    assert val == ""


# ---------- AC-B11: missing RESEND_API_KEY tolerated ----------
def test_rsvp_no_api_key_still_succeeds(client, app, monkeypatch):
    monkeypatch.setattr(app, "RESEND_API_KEY", None)
    payload = {"guests": [{"name": "Tom", "diet": "Ich esse alles", "allergies": ""}]}
    r = client.post("/invitation/rsvp", json=payload)
    assert r.status_code == 200
    assert r.get_json() == {"success": True}


# ---------- AC-B14: helper _save_guests_to_db returns UUID ----------
def test_save_guests_to_db_returns_uuid(app):
    guests = [{"name": "Foo", "diet": "Vegan", "allergies": ""}]
    sg = app._save_guests_to_db(
        guests,
        "invitation_rsvp",
        lambda g: {"diet": g["diet"], "allergies": g.get("allergies", "")},
    )
    uuid_mod.UUID(sg)


# ---------- AC-B15: _send_rsvp_email returns False without API key ----------
def test_send_rsvp_email_no_api_key(app, monkeypatch):
    monkeypatch.setattr(app, "RESEND_API_KEY", None)
    assert app._send_rsvp_email("subj", "body", "from@x.com") is False


def test_send_rsvp_email_with_api_key(app, monkeypatch):
    monkeypatch.setattr(app, "RESEND_API_KEY", "fake_key")
    monkeypatch.setattr(app.resend.Emails, "send", lambda payload: {"id": "1"})
    assert app._send_rsvp_email("subj", "body", "from@x.com") is True


# ---------- AC-B16, AC-B17: email content ----------
def test_invitation_email_subject_and_body(client, app, monkeypatch):
    captured = {}

    def fake_send(payload):
        captured.update(payload)
        return {"id": "1"}

    monkeypatch.setattr(app, "RESEND_API_KEY", "fake_key")
    monkeypatch.setattr(app.resend.Emails, "send", fake_send)

    payload = {"guests": [
        {"name": "Anna", "diet": "Vegetarisch", "allergies": "Nüsse"},
        {"name": "Tim", "diet": "Vegan", "allergies": ""},
        {"name": "Bob", "diet": "Ich esse alles", "allergies": ""},
    ]}
    r = client.post("/invitation/rsvp", json=payload)
    assert r.status_code == 200

    assert captured.get("subject", "").startswith("Einladung RSVP -")
    body = captured.get("text", "")
    assert "ERNÄHRUNG:" in body
    assert "Allesesser:" in body
    assert "Vegetarisch:" in body
    assert "Vegan:" in body


# ---------- AC-B18: email body shows "(keine Allergien gemeldet)" ----------
def test_invitation_email_no_allergies_section(client, app, monkeypatch):
    captured = {}

    def fake_send(payload):
        captured.update(payload)
        return {"id": "1"}

    monkeypatch.setattr(app, "RESEND_API_KEY", "fake_key")
    monkeypatch.setattr(app.resend.Emails, "send", fake_send)

    payload = {"guests": [{"name": "Lea", "diet": "Vegan", "allergies": ""}]}
    r = client.post("/invitation/rsvp", json=payload)
    assert r.status_code == 200
    body = captured.get("text", "")
    assert "(keine Allergien gemeldet)" in body
