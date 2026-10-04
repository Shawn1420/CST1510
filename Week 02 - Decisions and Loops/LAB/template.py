"""
RECORD CHECK  -  my version
===========================

Name  : Shawn Lugoloobi
Lane  : IT      (delete two)
Date  : 03/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
over_limit_count = 0

while True:
 label = input("Enter hostname (or 'quit' to stop): ")
 if label == "quit":
     break

 value = float(input("Enter GB used: "))  
 limit = float(input("Enter GB total: "))   

 difference = limit - value 
 percent = (value / limit)*100     

 if percent >= 100:
    status = "OVER LIMIT"
    over_limit_count += 1
 elif percent >= 90:
    status = "WARNING"
 else:
    status = "OK"

 print()
 print("=" * 34)
 print(f"  RECORD CHECK  -  {label}")
 print("=" * 34)
 print(f" {"Used":<10}: {value:>10.2f}")
 print(f" {"Total":<10}: {limit:>10.2f}")
 print(f" {"Free":<10}: {difference:>10.2f}")
 print(f" {"Percent":<10}: {percent:>10.2f} %")
 print(f" {"Status":<10}: {status:>10}")

 print("=" * 34)
print()
print(f"Records Over Limit this session: {over_limit_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
