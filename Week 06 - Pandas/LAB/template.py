"""
RECORD CHECK  -  my version
===========================

Name  : Shawn Lugoloobi
Lane  : IT
Date  : 06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import pandas as pd
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


folder = Path(__file__).parent

df = pd.read_csv(folder / "records.csv")
df["percent"] = (df["used_gb"] / df["total_gb"]) *100
print(df)

df["status"] = df["percent"].apply(
    lambda p: "OVERLIMIT" if p >= 100
    else ("WARNING" if p >= 90
          else "OK")
)
print()
print(df[df["status"] != "OK"])

counts = df.groupby("status").size()
print()
print(counts)

df.to_csv(folder / "records_report.csv", index=False)

counts.plot(kind="bar")
plt.title("Records per status")
plt.ylabel("Number of records")
plt.tight_layout()
plt.savefig(folder / "status_counts.png")