import sys
import csv
from tabulate import tabulate


# Exit via sys.exit if not exactly one command-line argumen or if file’s name does not end in .csv.
def main():
    if len(sys.argv) != 2:
        sys.exit("Too few arguments")
    elif (sys.argv[1]).endswith(".csv") == False:
        sys.exit("Not a csv file")
    else:
        print(grid())

def grid():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            return(tabulate(reader, headers="firstrow", tablefmt="grid"))
    # If file does not exist, raise FileNotFoundError and sys.exit
    except FileNotFoundError:
        sys.exit("File not found")
        
"""
# Tabulate documentation
>>> table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
...          ["Moon",1737,73.5],["Mars",3390,641.85]]
# Print with headers = keys and table format = grid
>>> print(tabulate({"Name": ["Alice", "Bob"],
...                 "Age": [24, 19]}, headers="keys", tablefmt="grid"))"""


if __name__ == "__main__":
    main()
