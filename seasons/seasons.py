from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    # Get brithday date
    dob = input("Date of Birth: ")
    # Print birthday as minutes, using inflect method
    print(days_to_minutes(dob))

def get_dob(s):
    # If birthday date is valid, convert to iso
    try:
        iso_date = date.fromisoformat(s)
    # If date is not valid, exit
    except:
        sys.exit("Invalid date")

    return (date.today() - iso_date).days

def days_to_minutes(days):
    minutes = 0
    # Convert days to minutes
    minutes = get_dob(days) * 60
    # Return minutes as a string
    return p.number_to_words(minutes)


if __name__ == "__main__":
    main()
