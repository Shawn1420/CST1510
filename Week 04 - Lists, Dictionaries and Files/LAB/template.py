"""
RECORD CHECK  -  my version
===========================

Name  : Shawn Lugoloobi
Lane  : IT
Date  : 17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check(value, limit):
    """Return the difference and the percentage of value against limit"""
    difference = limit - value
    percent = (value / limit) * 100
    if percent >= 100:
        status = "OVERLIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the bordered record check report"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(F"  {'Used' :<10}: {value:>10.2f}")
    print(F"  {'Total' :<10}: {limit:>10.2f}")
    print(F"  {'Free' :<10}: {difference:>10.2f}")
    print(F"  {'Percent' :<10}: {percent:>10.2f} %")
    print(F"  {'Status' :<10}: {status:>10}")
    print("=" * 34)

def load_records(path):
    """Read label, value, limit lines from a file and return a list of dicts"""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records 

def save_results(path, results):
    """Write one label,status line per result to a file"""
    with open(path, "w") as f:
        for result in results:
            f.write(f"{result['label']},{result['status']}\n")

try:
    records = load_records("records.txt")
except FileNotFoundError:
    print("records.txt not found - starting with no records")
    records = []

over_limit_count = 0
results = []

for record in records:
    difference, percent, status = check(record["limit"], difference, percent, status)
    results.append({"label": record["label"], "status": status})
    if status == "OVER LIMIT":
        over_limit_count += 1

save_results("results.txt", results)

print()
print(f"Records OVER LIMIT this session: {over_limit_count}")