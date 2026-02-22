import json
from datetime import datetime
from log_reader import follow
from detector import detect_bruteforce

def generate_alert(ip, attempts):

    timestamp = datetime.now().isoformat()

    if attempts >= 8:
        severity = "HIGH"
    else:
        severity = "MEDIUM"

    alert_data = {
        "timestamp": timestamp,
        "alert_type": "Brute Force Attempt",
        "source_ip": ip,
        "failed_attempts": attempts,
        "severity": severity
    }

    print(f"[ALERT] {alert_data}")

    with open("alerts.json", "a") as f:
        json.dump(alert_data, f)
        f.write("\n")

def main():
    with open("auth.log", "r") as logfile:
        loglines = follow(logfile)

        for line in loglines:
            result = detect_bruteforce(line)

            if result:
                ip, count = result
                generate_alert(ip, count)

if __name__ == "__main__":
    main()
