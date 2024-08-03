from datetime import date
import inflect

class Seasons:
    def __init__(self, date, minutes):
        self.date = date
        self.minutes = minutes

    def __str__(self):
        ...

    def calculate_minutes(self):
        ...

    @classmethod
    def get(cls):
        date = input("Date of Birth: ")
        return cls(date)

def main():
    ...




if __name__ == "__main__":
    main()