from collections import defaultdict


PACKET_LIMIT = 20
ip_packet_count = defaultdict(int)


def detect_suspicious_activity(source_ip):
    """Return alert message if packet count from IP is high."""
    if source_ip == "Unknown":
        return ""

    ip_packet_count[source_ip] += 1

    if ip_packet_count[source_ip] > PACKET_LIMIT:
        return f"Possible scan: high traffic from {source_ip}"

    return ""
