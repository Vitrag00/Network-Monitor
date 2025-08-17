# core/spoof_detector.py

import pandas as pd

def detect_mac_spoofing(baseline_path="data/baseline.csv", current_path="data/current_devices.csv"):
    base = pd.read_csv(baseline_path)
    current = pd.read_csv(current_path)

    alerts = []
    for _, row in current.iterrows():
        ip = row['IP']
        curr_mac = row['MAC']
        match = base[base['IP'] == ip]

        if not match.empty:
            orig_mac = match.iloc[0]['MAC']
            if curr_mac != orig_mac:
                alerts.append({
                    "IP": ip,
                    "Original MAC": orig_mac,
                    "Current MAC": curr_mac,
                    "Alert": "⚠ MAC Spoofing Suspected"
                })

    pd.DataFrame(alerts).to_csv("data/spoof_alerts.csv", index=False)
    print(f"[✔] Spoof detection complete. {len(alerts)} alerts saved.")
