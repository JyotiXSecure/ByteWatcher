# Simple IDS Project (Python)

This is a basic Intrusion Detection System (IDS) project made for learning.
It captures packets, checks simple suspicious behavior, and logs alerts.

## Features

- Packet sniffing using `scapy`
- Simple rule-based detection:
  - If one IP sends too many packets, mark it as suspicious
- CSV logging with:
  - `timestamp`, `source_ip`, `destination_ip`, `alert_message`
- Minimal dashboard using `streamlit` and `pandas`

## Project Files

- `sniffer.py` - captures packets and sends data for detection
- `detector.py` - basic if-else detection logic
- `logger.py` - writes logs to `logs.csv`
- `dashboard.py` - shows logs and alerts in Streamlit

## Install

```bash
pip install scapy pandas streamlit
```

## Run

1. Start packet sniffer:

```bash
python sniffer.py
```

2. In another terminal, run dashboard:

```bash
streamlit run dashboard.py
```

## Notes

- Run sniffer with admin privileges if packet capture fails.
- This is a beginner-level IDS, not a production security tool.
