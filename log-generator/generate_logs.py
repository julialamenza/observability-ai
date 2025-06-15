import time
import random
from datetime import datetime
import os

# Ensure consistent path across containers
LOG_FILE = "/app/log-generator/app.log"

levels = ["INFO", "WARNING", "ERROR"]

messages = {
    "INFO": ["Request successful", "Connection established", "Heartbeat OK"],
    "WARNING": ["Slow query detected", "Memory usage high", "Unusual response time"],
    "ERROR": ["Service unavailable", "Null pointer exception", "Out of memory"]
}

# Create log directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

while True:
    level = random.choices(levels, weights=[0.7, 0.2, 0.1])[0]
    msg = random.choice(messages[level])
    now = datetime.utcnow().isoformat()
    log_line = f"{level} {now} {msg}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_line)
    time.sleep(1)
