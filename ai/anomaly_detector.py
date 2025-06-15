import time
import os
from prometheus_client import start_http_server, Gauge

LOG_FILE = "/logs/app.log"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()

anomaly_gauge = Gauge('log_anomaly_detected', 'Anomaly detection flag: 1 if anomaly present')

def tail_log_file(path):
    with open(path, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

def detect_anomaly(line):
    return "ERROR" in line and "Shift test" in line

def monitor_for_anomalies():
    for line in tail_log_file(LOG_FILE):
        print("Analyzing:", line)
        if detect_anomaly(line):
            anomaly_gauge.set(1)
        else:
            anomaly_gauge.set(0)

if __name__ == "__main__":
    print("🧠 Anomaly detector running on port 8100...")
    start_http_server(8100)
    monitor_for_anomalies()
