import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.search(
        # <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
        r'^<iframe src="https?:\/\/(?:www\.)?youtube\.com\/embed\/([a-z0-9_]+)"><\/iframe>', s, re.IGNORECASE
        ):
        # https://youtu.be/xvFZjo5PgG0
        return (f"https://youtu.be/{matches.group(1)}")
    else:
        return None



if __name__ == "__main__":
    main()
