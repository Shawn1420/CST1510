"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
from pathlib import Path

folder = Path(__file__).parent

def parse_line(raw_line):
    """Strip and lowercase one raw line and return a dict with clean keys and float values"""
    hostname_part, rest = raw_line.strip().lower().split(",", 1)
    record = {"hostname": hostname_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())
    return record

def status_of(used, total):
    """Return OVER LIMIT, WARNING or OK from the GB used and GB total"""
    percentage = used / total * 100
    if percentage >= 100:
        return "OVER LIMIT"
    if percentage >= 90:
        return "WARNING"
    return "OK"

def load_lines(path):
    """Readnthe file at path and return its filled lines"""
    with open(path) as f:
        return [line for line in f if line.strip()]

def print_record(record, status):
    """Print one cleaned record with its status"""
    print(f"{record['hostname']:<10} used={record['used']:>8.1f} total={record['total']:>8.1f} {status}")

def print_summary(total_records, flagged):
    """Print a one-line summary of records checked and records flagged"""
    print(f"Summary: {total_records} records, {flagged} flagged")

raw_lines = load_lines(folder / "raw_lines.txt")
parsed = 0
flagged = 0

for raw in raw_lines:
    try:
        record = parse_line(raw)
    except ValueError:
        print("could not parse:", raw.strip())
        continue
    status = status_of(record["used"], record["total"])
    print(record)
    print_record(record, status)
    print_record(record, status)
    parsed += 1
    if status != "OK":
        flagged += 1

print()
print_summary(parsed, flagged)