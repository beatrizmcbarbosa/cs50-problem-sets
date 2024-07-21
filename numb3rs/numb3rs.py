import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    # Typical format #.#.#.#, each # is a number between 0 and 255 (not included)
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"
    match = re.search(pattern, ip)

    if match:
        for i in range(1, 5):
            if int(match.group(i)) > 255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()
