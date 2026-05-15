"""Shared fixtures for backend tests.

Imports `application` exactly once at module load (Flask app is a singleton),
forces a temp SQLite DB, removes any RESEND_API_KEY from the environment,
and exposes a Flask test client + DB-reset fixture.
"""
import os
import sqlite3
import sys
import tempfile

import pytest

# Use a temp SQLite DB; ensure no Postgres
_TMP_DB = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
_TMP_DB.close()
os.environ["DATABASE_URL"] = ""
os.environ["LOCAL_DB_PATH"] = _TMP_DB.name
os.environ.pop("RESEND_API_KEY", None)
os.environ.setdefault("SAVE_THE_DATE_PASSWORD", "150826")
os.environ.setdefault("SAVE_THE_DATE_FAMILY_PASSWORD", "140826")

# Project root must be importable
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import application as app_mod  # noqa: E402
app_mod.server.config["TESTING"] = True

TEST_DB_PATH = _TMP_DB.name


@pytest.fixture
def app():
    return app_mod


@pytest.fixture
def client():
    with app_mod.server.test_client() as c:
        yield c


@pytest.fixture(autouse=True)
def reset_db():
    """Wipe both tables before each test. Ensures init_db ran."""
    app_mod.init_db()
    conn = sqlite3.connect(TEST_DB_PATH)
    cur = conn.cursor()
    for table in ("rsvp", "invitation_rsvp"):
        try:
            cur.execute(f"DELETE FROM {table}")
        except sqlite3.OperationalError:
            pass
    conn.commit()
    conn.close()
