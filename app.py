import re
from collections import defaultdict
from flask import Flask, render_template_string

app = Flask(__name__)

LOG_FILE = "auth.log"

def analyze_logs():
    failed_attempts = defaultdict(int)
    pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

    with open(LOG_FILE, "r") as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1

    suspicious = []
    for ip, count in failed_attempts.items():
        if count >= 5:
            suspicious.append((ip, count))

    return suspicious

@app.route("/")
def home():
    suspicious = analyze_logs()
    total_alerts = len(suspicious)

    return render_template_string("""
        <h1>Mini SIEM Dashboard</h1>
        <h2>Total Suspicious IPs: {{ total }}</h2>
        <hr>
        {% for ip, count in suspicious %}
            <p><b>{{ ip }}</b> - {{ count }} failed attempts</p>
        {% endfor %}
    """, suspicious=suspicious, total=total_alerts)

if __name__ == "__main__":
    app.run(debug=True)
