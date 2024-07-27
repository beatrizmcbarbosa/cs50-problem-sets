import re

def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    if match := re.findall(r"\bum*", s):
        for match in s:
            count += 1
        return count


if __name__ == "__main__":
    main()
