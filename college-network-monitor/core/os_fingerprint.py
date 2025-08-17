# core/os_fingerprint.py

from scapy.all import IP, TCP, sr1
import pandas as pd
from mac_vendor_lookup import MacLookup

def guess_os(ttl, win):
    if ttl >= 128:
        return "Windows"
    elif ttl >= 64:
        return "Linux/Android"
    elif ttl >= 255:
        return "Cisco/Network Device"
    else:
        return "Unknown"

def fingerprint_device(ip):
    try:
        pkt = IP(dst=ip)/TCP(dport=80, flags='S')
        resp = sr1(pkt, timeout=1, verbose=0)
        if resp:
            return {
                "TTL": resp.ttl,
                "WinSize": resp.window,
                "OS": guess_os(resp.ttl, resp.window)
            }
    except:
        pass
    return {
        "TTL": None,
        "WinSize": None,
        "OS": "Unreachable"
    }

def fingerprint_all(file_path="data/current_devices.csv"):
    df = pd.read_csv(file_path)
    mac_lookup = MacLookup()
    try:
        mac_lookup.update_vendors()
    except:
        pass

    results = []
    for _, row in df.iterrows():
        ip = row['IP']
        mac = row['MAC']
        os_data = fingerprint_device(ip)
        try:
            vendor = mac_lookup.lookup(mac)
        except:
            vendor = "Unknown"

        results.append({
            "IP": ip,
            "MAC": mac,
            "Vendor": vendor,
            **os_data
        })

    pd.DataFrame(results).to_csv("data/baseline.csv", index=False)
    print("[✔] OS fingerprinting complete. Results saved to baseline.csv")
