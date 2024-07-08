import csv, sys

def main():
    # If not 3 arguments, exit
    if len(sys.argv) != 3:
        sys.exit("Too few or many arguments.")
    # Else scourgify
    else:
        print(scourgify())

def scourgify():
    # Open file and read "name" and "house"
    list = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        try:
            for name, house in reader:
                first, last = name.split(",")
                list.append({"first": first, "last": last, "house": house})
                # Split "name" into "first" and "last" and write that and "house" into argv[3]
                with open(sys.argv[3], "a") as newfile:
                    writer = csv.DictWriter(newfile, fieldnames["first", "last", "house"])
                    writer.writerow({"first": first, "last": last, "house": house})
        # If not readable, exit
        except FileNotFoundError:
            sys.exit("File not readable")


if __name__ == "__main__":
    main()
