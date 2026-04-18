from datetime import datetime

from scapy.all import IP, sniff

from detector import detect_suspicious_activity
from logger import setup_log_file, write_log


def protocol_name(packet):
    """Map protocol number to simple name."""
    protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
    return protocol_map.get(packet[IP].proto, "OTHER")


def handle_packet(packet):
    """Read packet info, check for alert, and log."""
    if IP not in packet:
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    protocol = protocol_name(packet)
    alert = detect_suspicious_activity(source_ip)
    message = alert if alert else f"Normal traffic ({protocol})"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    write_log(timestamp, source_ip, destination_ip, message)
    print(f"{timestamp} | {source_ip} -> {destination_ip} | {message}")


def start_sniffer():
    """Start packet capture."""
    setup_log_file()
    print("Sniffer started... Press Ctrl + C to stop.")
    sniff(prn=handle_packet, store=False)


if __name__ == "__main__":
    start_sniffer()
