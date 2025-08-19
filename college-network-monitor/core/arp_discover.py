# core/arp_discover.py

from scapy.all import arping
import pandas as pd

def discover_devices(subnet="192.168.29.33/24"):
    print(f"[+] Scanning subnet: {subnet}")
    ans, _ = arping(subnet, verbose=0)
    
    devices = []
    for _, received in ans:
        devices.append({
            "IP": received.psrc,
            "MAC": received.hwsrc
        })

    df = pd.DataFrame(devices)
    df.to_csv("data/baseline.csv", index=False)
    print(f"[✔] Discovered {len(devices)} devices. Saved to current_devices.csv")
