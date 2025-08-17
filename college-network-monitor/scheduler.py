# scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from core.arp_discover import discover_devices
from core.os_fingerprint import fingerprint_all
from core.spoof_detector import detect_mac_spoofing
from core.passive_sniffer import start_sniffer

import time

def run_all():
    print("[*] Running network monitoring tasks...")
    discover_devices()
    fingerprint_all()
    detect_mac_spoofing()
    start_sniffer(limit=1000)

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_all, 'interval', minutes=10)
    scheduler.start()

    print("[*] Scheduler started. Monitoring every 10 mins.")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        scheduler.shutdown()
