# Mini SIEM – SSH Brute Force Detection

This project simulates a basic Security Information and Event Management (SIEM) system by analyzing Linux authentication logs to detect SSH brute-force attacks.

## Features

- Parses Linux auth.log file
- Detects failed SSH login attempts
- Flags suspicious IPs with 5+ failed attempts
- Displays alerts in a simple Flask web dashboard

## Technologies Used

- Python
- Regex
- Flask
- Log Analysis

## How It Works

The system scans authentication logs, extracts IP addresses from failed login attempts, counts occurrences, and generates alerts for suspicious behavior.

## Future Improvements

- Real-time log monitoring
- Email alert system
- Database integration
- Visualization charts
