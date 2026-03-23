import subprocess
import time
import sys
from datetime import datetime
from colorama import Fore, Style, init

# Initialize Colorama for Windows terminal
init(autoreset=True)

TARGET = "8.8.8.8"
LOG_FILE = "network_incidents.log"
TIMEOUT_MS = "1000" # 1 second timeout for faster detection

def log_incident(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def check_network():
    try:
        # Using -w to set a 1-second timeout (Professional standard)
        cmd = f"ping -n 1 -w {TIMEOUT_MS} {TARGET}"
        output = subprocess.check_output(cmd, shell=True).decode()
        
        if "time=" in output:
            ms = output.split("time=")[1].split("ms")[0].strip()
            ms_int = int(ms)
            
            # Color coding based on latency thresholds
            if ms_int < 50:
                print(f"{Fore.GREEN}[OK] {datetime.now().strftime('%H:%M:%S')} - Latency: {ms}ms")
            elif ms_int < 150:
                print(f"{Fore.YELLOW}[WARNING] {datetime.now().strftime('%H:%M:%S')} - High Latency: {ms}ms")
            else:
                print(f"{Fore.RED}[CRITICAL] {datetime.now().strftime('%H:%M:%S')} - Severe Lag: {ms}ms")
            return True
        return False
    except subprocess.CalledProcessError:
        return False

def main():
    print(f"{Fore.CYAN}=== ENTERPRISE NETWORK MONITOR STARTING ===")
    print(f"Target: {TARGET} | Timeout: {TIMEOUT_MS}ms\n")
    
    is_down = False
    down_time = None

    while True:
        if check_network():
            if is_down:
                # Network just came back up!
                up_time = datetime.now()
                duration = up_time - down_time
                msg = f"NETWORK RESTORED. Total downtime: {duration}"
                print(f"{Fore.CYAN}{Style.BRIGHT}{msg}")
                log_incident(msg)
                is_down = False
        else:
            if not is_down:
                # Network just went down!
                down_time = datetime.now()
                msg = "NETWORK DOWN - Incident Started"
                print(f"{Fore.RED}{Style.BRIGHT}!!! {msg} !!!")
                log_incident(msg)
                is_down = True
            else:
                print(f"{Fore.RED}[OFFLINE] {datetime.now().strftime('%H:%M:%S')} - Retrying...")

        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.WHITE}Monitoring terminated by user.")
        sys.exit()