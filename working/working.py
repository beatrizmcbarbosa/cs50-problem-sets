import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    if matches:= re.search(r"(\d{1,2})\:?(\d{1,2})? (AM|PM) to (\d{1,2})\:?(\d{1,2})? (AM|PM)", s):
        # separate hours from minutes, minutes will be the same. Group 2 and Group 5
        if matches.group(2) is not None:
            minutesFrom = int(matches.group(2))
        else:
            minutesFrom = 00
        if matches.group(5) is not None:
            minutesTo = int(matches.group(5))
        else:
            minutesTo = 00

        # if it is AM, then result is the same. If it is PM, result is number + 12
        if matches.group(3) == "AM":
            hoursFrom = int(matches.group(1))
        else:
            hoursFrom = int(matches.group(1)) + 12
        if matches.group(6) == "AM":
            hoursTo = int(matches.group(4))
        else:
            hoursTo = int(matches.group(4)) + 12
    #print(f"{n:02}")
    return(f"{hoursFrom:02}:{minutesFrom:02} to {hoursTo:02}:{minutesTo:02}")


if __name__ == "__main__":
    main()
