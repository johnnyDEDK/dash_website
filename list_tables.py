#!/usr/bin/env python3
"""List database tables and sample contents using SQLAlchemy.

Usage:
  python list_tables.py --url <DATABASE_URL> [--limit 100]
Or set environment variable DATABASE_URL.
"""
import os
import argparse
import json
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy import inspect


def main():
    parser = argparse.ArgumentParser(description="List DB tables and their rows")
    parser.add_argument("--url", help="Database URL (overrides DATABASE_URL env var)")
    parser.add_argument("--limit", type=int, default=100, help="Max rows to show per table")
    args = parser.parse_args()

    db_url = args.url or os.getenv("DATABASE_URL")
    if not db_url:
        print("Error: Provide a database URL via --url or DATABASE_URL env var")
        return

    engine = create_engine(db_url)
    inspector = inspect(engine)

    try:
        tables = inspector.get_table_names()
    except Exception as e:
        print(f"Error listing tables: {e}")
        return

    if not tables:
        print("No tables found.")
        return

    print("Tables:")
    for t in tables:
        print(f" - {t}")

    print("\nFetching contents (up to {} rows per table):\n".format(args.limit))

    meta = MetaData()
    meta.reflect(bind=engine, only=tables)

    with engine.connect() as conn:
        for tname in tables:
            print(f"== Table: {tname} ==")
            try:
                table = Table(tname, meta, autoload_with=engine)
                stmt = select(table).limit(args.limit)
                result = conn.execute(stmt)
                rows = [dict(r) for r in result]
                if not rows:
                    print("(no rows)")
                else:
                    print(json.dumps(rows, default=str, indent=2))
            except Exception as e:
                print(f"Error reading table {tname}: {e}")
            print()


if __name__ == "__main__":
    main()
