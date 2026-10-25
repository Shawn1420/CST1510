"""
RECORD CHECK  -  my version
===========================

Name  : Shawn Lugoloobi
Lane  : IT
Date  : 22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit 
    def difference(self):
        """Return how many GB are free"""
        return self.limit - self.value 
    def percent(self):
        """Return the GB used as a percentage of the GB total"""
        return(self.value / self.limit) * 100
    def status(self):
        """Return OVER LIMIT, WARNING or OK based on the percentage"""
        percent = self.percent()
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

def load_records(path):
    """Read label, value, limit lines from a file and return a list of Record objects"""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            label, value, limit = line.split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

def print_report(record,status):
    """Print the bordered report for one record"""
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f" {'Used':<10}: {record.value:>10.2f}")
    print(f" {'Total':<10}: {record.limit:>10.2f}")
    print(f" {'Free':<10}: {record.difference():>10.2f}")
    print(f" {'Percent':<10}: {record.percent():>10.2f} %")
    print("=" * 34)

records = load_records("records.txt")
over_limit_count = 0

for record in records:
    status = record.status()
    print_report(record, status)
    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Records OVER LIMIT this session: {over_limit_count}")

