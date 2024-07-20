#!/usr/bin/python3
"""
0x03. Log Parsing
"""
import sys
import re
import signal


total_file_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

line_count = 0


def print_statistics():
    """Prints the accumulated metrics"""
    print(f"File size: {total_file_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal (CTRL+C)"""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            status = parts[-2]
            size = parts[-1]

            if re.match(r"\d+", status) and re.match(r"\d+", size):
                if status in status_counts:
                    status_counts[status] += 1
                total_file_size += int(size)
                line_count += 1

            if line_count % 10 == 0:
                print_statistics()

        except Exception as e:
            continue

except Exception as e:
    pass

print_statistics()
