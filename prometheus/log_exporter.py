from prometheus_client import start_http_server, Counter
import time
import os

LOG_FILE = "/app/log-generator/app.log"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()

# Use Counter instead of Gauge
error_count = Counter('log_error_count', 'Number of ERROR log entries')
warning_count = Counter('log_warning_count', 'Number of WARNING log entries')

def tail_log_file(path):
    with open(path, 'r') as f:
        f.seek(0)  # read from beginning (better for initial testing)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

def monitor_logs():
    for line in tail_log_file(LOG_FILE):
        print("Reading line:", line.strip())
        if "ERROR" in line:
            error_count.inc()
        elif "WARNING" in line:
            warning_count.inc()

if __name__ == "__main__":
    print("🚀 Starting Prometheus log exporter on http://localhost:8000/metrics")
    start_http_server(8000)
    monitor_logs()
