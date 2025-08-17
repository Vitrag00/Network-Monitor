# core/usage_tracker.py

import pandas as pd

def summarize_usage(path="data/usage_logs.csv"):
    df = pd.read_csv(path)
    df['Total'] = df['Sent'] + df['Received']
    df = df.sort_values(by="Total", ascending=False)
    print("[*] Top 5 data consumers:")
    print(df.head())
