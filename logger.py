import csv
from pathlib import Path


LOG_FILE = Path("logs.csv")


def setup_log_file():
    """Create log file with header if missing."""
    if not LOG_FILE.exists():
        with LOG_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["timestamp", "source_ip", "destination_ip", "alert_message"])


def write_log(timestamp, source_ip, destination_ip, alert_message):
    """Append one log row to CSV."""
    with LOG_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, source_ip, destination_ip, alert_message])
