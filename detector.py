import re
from collections import defaultdict

failed_attempts = defaultdict(int)

def detect_bruteforce(line, threshold=5):
    pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
    match = re.search(pattern, line)

    if match:
        ip = match.group(1)
        failed_attempts[ip] += 1

        if failed_attempts[ip] >= threshold:
            return ip, failed_attempts[ip]

    return None
