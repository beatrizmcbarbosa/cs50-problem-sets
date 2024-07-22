import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(
        # https://www.youtube.com/embed/xvFZjo5PgG0
        r"^https?:\/\/(?:www\.)?youtube\.com\/embed\/([a-z0-9_]+)", s, re.IGNORECASE
        ):
        return (f"https://youtu.be/{matches.group(1)}")
    else:
        return None



if __name__ == "__main__":
    main()
