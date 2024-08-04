from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    # Get brithday date
    dob = input("Date of Birth: ")
    # Print birthday as minutes, using inflect method
    print(days_to_minutes(dob))

def det_dob(s):
    # If birthday date is valid, convert to iso
    try:
        iso_date = date.fromisoformat(s)
    # If date is not valid, exit
    except:
        sys.exit("Invalid date")
    # Return days
    return (date.today - iso_date).day


def days_to_minutes():
    # Subtract birthday from today's date, using timedelta. Today's date is given by date class
    ...
    # Convert days to minutes
    ...


if __name__ == "__main__":
    main()
