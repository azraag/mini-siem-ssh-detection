from log_reader import follow
from detector import detect_bruteforce

def main():
    with open("auth.log", "r") as logfile:
        loglines = follow(logfile)

        for line in loglines:
            result = detect_bruteforce(line)

            if result:
                ip, count = result
                print(f"[ALERT] Possible brute force from {ip} ({count} attempts)")

if __name__ == "__main__":
    main()
