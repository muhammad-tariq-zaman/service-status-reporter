"""Check TCP services listed in a CSV (name,host,port) and report UP/DOWN.

Usage: python3 main.py services.csv
"""
import argparse
import csv
import socket
import sys


def check(host, port, timeout=2.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="CSV file with name,host,port columns")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    up = 0
    for row in rows:
        ok = check(row["host"], int(row["port"]))
        up += ok
        print(f"{row['name']}: {'UP' if ok else 'DOWN'} ({row['host']}:{row['port']})")
    print(f"{up}/{len(rows)} services up.")
    return 0 if up == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
