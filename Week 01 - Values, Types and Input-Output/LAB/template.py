"""
RECORD CHECK  -  my version
===========================

Name  : Shawn Lugoloobi
Lane  : IT      
Date  : 23/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label = input("Enter your hostname: ")
first = float(input("Enter your GB used: "))
second = float(input("Enter your GB total: "))


difference = second - first 
percent = (first / second)*100

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  {"Used":<10}: {first:>10.2f}")
print(f"  {"Total":<10}: {second:>10.2f}")
print(f"  {"Free":<10}: {difference:>10.2f}")
print(f"  {"Percent":<10}: {percent:>10.2f}%")

print("=" * 34)