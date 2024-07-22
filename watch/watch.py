import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(
        r"^https?://(?:www\.)?youtube\.com/([a-z0-9_]+)", s, re.IGNORECASE
        ):
        return "https://youtu.be/"
    else:
        return None



if __name__ == "__main__":
    main()
