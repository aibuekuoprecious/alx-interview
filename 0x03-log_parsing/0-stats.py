#!/usr/bin/python3

import sys


def print_stats(total_size, status_codes):
    print("Total file size: File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(code, ":", status_codes[code])


def parse_log():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            if count > 10:
                print_stats(total_size, status_codes)
                count = 1

            parts = line.split()
            if len(parts) >= 7:
                size = int(parts[-1])
                code = int(parts[-2])
                total_size += size
                if code in status_codes:
                    status_codes[code] += 1

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    parse_log()
