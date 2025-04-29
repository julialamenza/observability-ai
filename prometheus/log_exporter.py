import time
from prometheus_client import start_http_server, Gauge
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(script_dir, "../log-generator/app.log")

# Define Prometheus metrics
error_count = Gauge('log_error_count', 'Number of ERROR log entries')
warning_count = Gauge('log_warning_count', 'Number of WARNING log entries')

def tail_log_file(path):
    with open(path, 'r') as f:
        # Read from beginning
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

def monitor_logs():
    err = 0
    warn = 0
    for line in tail_log_file(LOG_FILE):
        print("Reading line:", line.strip())  # cleaner print
        if "ERROR" in line:
            err += 1
        elif "WARNING" in line:
            warn += 1

        # Update Prometheus metrics
        error_count.set(err)
        warning_count.set(warn)

if __name__ == "__main__":
    print("Starting Prometheus exporter on http://localhost:8000/metrics")
    start_http_server(8000)
    monitor_logs()
