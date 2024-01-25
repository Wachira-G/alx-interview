#!/usr/bin/python3

"""Reads stdin line by line and computes metrics."""
import re
import signal
import sys

status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
}

file_size = 0
counter = 1
pattern = (
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} '
    r'\d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/\d+ HTTP/1\.1" \d+ \d+'
)


for line in sys.stdin:
    if re.match(pattern, line):
        status_code = int(line.split()[7])
        status_codes[status_code] += 1
        file_size += int(line.split()[8])

    if counter % 10 == 0:
        print(f"File size: {file_size}")
        for k, v in status_codes.items():
            if v > 0:
                print(f"{k}: {v}")

    counter += 1


def signal_handler(sig, frame):
    """Handles ctrl + c signal."""
    print(f"File size: {file_size}")
    for k, v in status_codes.items():
        if v > 0:
            print(f"{k}: {v}")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
