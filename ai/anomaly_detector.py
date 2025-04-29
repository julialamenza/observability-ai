import time
from datetime import datetime, timedelta
from collections import deque
from prometheus_client import start_http_server, Gauge

LOG_FILE = "log-generator/app.log"
WINDOW_SECONDS = 60
ERROR_THRESHOLD = 10

# Prometheus metric
anomaly_gauge = Gauge('log_anomaly_detected', 'Anomaly detection flag: 1 if anomaly present')

def tail_log_file(path):
    with open(path, 'r') as f:
        f.seek(0, 2)  # Move to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line.strip()

def monitor_for_anomalies():
    error_timestamps = deque()

    for line in tail_log_file(LOG_FILE):
        if "ERROR" in line:
            now = datetime.utcnow()
            error_timestamps.append(now)

            # Remove old entries outside the time window
            while error_timestamps and (now - error_timestamps[0]) > timedelta(seconds=WINDOW_SECONDS):
                error_timestamps.popleft()

            if len(error_timestamps) > ERROR_THRESHOLD:
                print(f"⚠️  Anomaly detected! {len(error_timestamps)} ERRORs in the last {WINDOW_SECONDS} seconds")
                anomaly_gauge.set(1)
                time.sleep(5)
                anomaly_gauge.set(0)
                error_timestamps.clear()

if __name__ == "__main__":
    print("🧠 Anomaly detector running on port 8100...")
    start_http_server(8100)  # Prometheus will scrape this
    monitor_for_anomalies()
