import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Typical format #.#.#.#, each # is a number between 0 and 255 (not included)
    pattern = r"^[1-255].[1-255].[1-255].[1-255]"
    match = re.search(pattern, ip, re.IGNORECASE)

    if match:
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
