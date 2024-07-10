def main():
    plate = input("Plate: ").casefold()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # char must be between 2 and 6 characters, and no special characters. All vanity plates must start with at least two letters
    if len(s) >= 2 and len(s) <= 6:
        if s.isalpha():
            return True
        elif s[0:2].isalpha() and s.isalnum():
            for char in s:
                #char must be numeric but first character can't be 0
                if char.isnumeric():
                    index=s.index(char)
                    if s[index:].isnumeric() and  int(char) != 0:
                        return True
                    else:
                        return False

if __name__ == "__main__":
    main()