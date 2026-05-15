#!/usr/bin/env python3
"""Safely delete rows by id from the `rsv` table using SQLAlchemy.

Usage examples:
  # Dry run (default) — shows rows that would be deleted
  python delete_rsv.py --ids 1,2,3

  # Actually delete (non-reversible) after confirmation flag
  python delete_rsv.py --ids 1,2,3 --yes

  # Provide DB URL via env var
  DATABASE_URL="sqlite:///local_rsvp.db" python delete_rsv.py --ids 5

Options:
  --url    Database URL (overrides DATABASE_URL env var)
  --ids    Comma-separated ids to delete
  --file   File containing one id per line or comma-separated
  --yes    Skip confirmation and perform delete
  --dry-run  Show rows that would be deleted (default)

Note: the script will try to detect the primary key column; if none
is found it will use a column named "id".
"""

import os
import argparse
import json
from sqlalchemy import create_engine, MetaData, Table, select, delete
from sqlalchemy import inspect
from sqlalchemy import URL, create_engine


def parse_id_list(s):
    if not s:
        return []
    parts = [p.strip() for p in s.split(",") if p.strip()]
    ids = []
    for p in parts:
        try:
            ids.append(int(p))
        except ValueError:
            ids.append(p)
    return ids


def ids_from_file(path):
    with open(path, "r", encoding="utf8") as fh:
        content = fh.read()
    # allow comma-separated or newline-separated
    content = content.replace("\r", "\n")
    lines = []
    for part in content.split("\n"):
        if not part:
            continue
        for p in part.split(","):
            if p.strip():
                lines.append(p.strip())
    return [int(x) if x.isdigit() else x for x in lines]


def main():
    parser = argparse.ArgumentParser(description="Delete specific ids from rsv table")
    parser.add_argument("--url", help="Database URL (overrides DATABASE_URL env var)")
    parser.add_argument("--ids", help="Comma-separated ids to delete")
    parser.add_argument("--file", help="File with ids (one per line or comma-separated)")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation and perform delete")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Show rows without deleting (default)")
    args = parser.parse_args()


    ids = []
    if args.ids:
        ids = parse_id_list(args.ids)
    elif args.file:
        ids = ids_from_file(args.file)
    else:
        print("Error: specify --ids or --file with ids to delete")
        return

    if not ids:
        print("No ids provided")
        return

    connection_string = URL.create(
        'postgresql',
        username='koyeb-adm',
        password='npg_quhZXOE5WPU9',
        host='ep-morning-darkness-age1f0uo.c-2.eu-central-1.pg.koyeb.app',
        database='koyebdb',
    )
    engine = create_engine(connection_string)
    inspector = inspect(engine)

    try:
        tables = inspector.get_table_names()
    except Exception as e:
        print(f"Error inspecting database: {e}")
        return

    if "rsvp" not in tables:
        print("Table 'rsv' not found in the database.")
        return

    meta = MetaData()
    meta.reflect(bind=engine, only=["rsvp"])
    table = Table("rsvp", meta, autoload_with=engine)

    # determine primary key or fallback to 'id'
    pk_cols = [c for c in table.primary_key.columns]
    if len(pk_cols) == 1:
        pk_col = pk_cols[0]
    else:
        if "id" in table.c:
            pk_col = table.c.id
        else:
            print("Could not determine single primary key column for 'rsvp'.")
            return

    with engine.connect() as conn:
        stmt = select(table).where(pk_col.in_(ids))
        found = conn.execute(stmt).mappings().all()

        if not found:
            print("No matching rows found for provided ids.")
            return

        print("Found rows:")
        print(json.dumps([dict(r) for r in found], default=str, indent=2))

        if not args.yes:
            resp = input("Proceed to delete these rows? Type 'yes' to confirm: ")
            if resp.strip().lower() != "yes":
                print("Aborted — no rows deleted.")
                return

    # perform delete inside a transaction
    try:
        with engine.begin() as conn:
            del_stmt = delete(table).where(pk_col.in_(ids))
            res = conn.execute(del_stmt)
            print(f"Deleted {res.rowcount} rows from 'rsv'.")
    except Exception as e:
        print(f"Error during delete: {e}")


if __name__ == "__main__":
    main()
