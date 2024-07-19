import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Typical format #.#.#.#, each # is a number between 0 and 255 (not included)
    match = r""
    if match:
        return True
    else:
        return false


...


if __name__ == "__main__":
    main()
