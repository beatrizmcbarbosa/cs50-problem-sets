def main():
    while True:
        try:
            percentage = convert(input('Fraction: '))
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percentage))

# convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and
# returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
# If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
# If Y is 0, then convert should raise a ZeroDivisionError.
def convert(fraction):
    x, y = fraction.split("/")

    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError

    return round((int(x) / int(y)) * 100)


# gauge expects an int and returns a str that is:
# "E" if that int is less than or equal to 1,
# "F" if that int is greater than or equal to 99,
# and "Z%" otherwise, wherein Z is that same int.
def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    elif 1 < percentage < 99:
        return f'{percentage}%'

if __name__ == "__main__":
    main()
