"""
RECORD CHECK  -  my version
===========================

Name  : Shawn Daniel Gitta Lugoloobi
Lane  : IT     
Date  : 11/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    if percent >= 100:
        return "OVERLIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Return the difference and the percentage of value against limit"""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


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

over_limit_count = 0

while True:

    label = input("Enter hostname (or 'quit' to stop): ")
    if label == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter GB total: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVERLIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)

print()
print(f"Records OVERLIMIT this session: {over_limit_count}")
