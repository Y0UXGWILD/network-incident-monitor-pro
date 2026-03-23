# Enterprise Network Incident Monitor (Python-Based)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Network Engineering](https://img.shields.io/badge/Field-Networking%20Automation-orange.svg)

## Project Overview
As a Networking Engineer, I developed this tool to bridge the gap between manual troubleshooting and enterprise-grade monitoring. This Python-based utility automates the detection of network outages, measures real-time latency (jitter), and maintains an automated incident log for ISP accountability and SLA (Service Level Agreement) tracking.



## Key Features
* **Real-Time Latency Thresholding:** Categorizes network health into **OK (<50ms)**, **Warning (50-150ms)**, and **Critical (>150ms)** using color-coded CLI output.
* **Automated Incident Logging:** Records the exact timestamp of "Network Down" events and calculates total downtime duration upon restoration.
* **Fault Isolation:** Designed to help engineers distinguish between local hardware failure and upstream ISP congestion (Bufferbloat).
* **Optimized Resource Footprint:** Utilizes low-level subprocess calls and adjustable polling intervals to ensure zero impact on system performance.

## Technical Stack
* **Language:** Python 3.10+
* **Libraries:** `subprocess` (for OS-level ICMP requests), `colorama` (for professional CLI visualization), `datetime` (for precise incident tracking).
* **Environment:** Cross-platform compatibility (Windows/Linux).

## Sample Output
```text
=== ENTERPRISE NETWORK MONITOR STARTING ===
[OK] 17:05:10 - Latency: 22ms
[WARNING] 17:05:12 - High Latency: 125ms
!!! NETWORK DOWN - Incident Started !!!
[OFFLINE] 17:05:14 - Retrying...
NETWORK RESTORED. Total downtime: 0:00:15
