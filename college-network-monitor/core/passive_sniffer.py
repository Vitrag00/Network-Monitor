# core/passive_sniffer.py

from scapy.all import sniff, IP
from collections import defaultdict
import pandas as pd

data_usage = defaultdict(lambda: {"Sent": 0, "Received": 0})

def monitor_packet(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        size = len(pkt)

        if ip_src.startswith("192.168."):
            data_usage[ip_src]["Sent"] += size
        if ip_dst.startswith("192.168."):
            data_usage[ip_dst]["Received"] += size

def start_sniffer(limit=5000):
    print("[*] Passive sniffer started...")
    sniff(filter="ip", prn=monitor_packet, count=limit, store=0)

    # Save results
    df = pd.DataFrame.from_dict(data_usage, orient='index').reset_index()
    df.columns = ["IP", "Sent", "Received"]
    df.to_csv("data/usage_logs.csv", index=False)
    print("[✔] Data usage logged in usage_logs.csv")
