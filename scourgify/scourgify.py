import csv, sys

def main():
    # If not 3 arguments, exit
    if len(sys.argv) != 2:
        sys.exit("Too few or many arguments.")
    # Else scourgify
    else:
        print(scourgify())

def scourgify():
    # Open file and read "name" and "house"
    list = []
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        try:
            for name, house in reader:
                list.append({"name": name, "house": house})
            return name, house
        except FileNotFoundError:
            sys.exit("File not readable")
    # If not readable, exit
    # Split "name" into "first" and "last" and write that and "house" into argv[3]

if __name__ == "__main__":
    main()
