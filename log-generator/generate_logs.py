import time
import random
from datetime import datetime, UTC


LEVELS = ["INFO", "WARNING", "ERROR"]

def generate_log_line():
    level = random.choices(LEVELS, weights=[0.7, 0.2, 0.1])[0]
    now = datetime.now(UTC).isoformat()
    if level == "INFO":
        msg = "Request successful"
    elif level == "WARNING":
        msg = "Slow query detected"
    else:
        msg = "Database connection failed"
    return f"{level} {now} {msg}"

if __name__ == "__main__":
    with open("log-generator/app.log", "a") as f:
        while True:
            # Occasionally simulate a burst of errors
            if random.random() < 0.05:  # 5% chance
                print("💥 Injecting error burst...")
                for _ in range(random.randint(5, 10)):
                    now = datetime.now(UTC).isoformat()
                    f.write(f"ERROR {now} Simulated anomaly error\n")
                    f.flush()
                    time.sleep(0.1)
            else:
                log_line = generate_log_line()
                f.write(log_line + "\n")
                f.flush()
                time.sleep(1)
