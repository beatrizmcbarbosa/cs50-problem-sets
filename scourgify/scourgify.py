import csv, sys

def main():
    # If not 3 arguments, exit
    if len(sys.argv) != 3:
        sys.exit("Too few or many arguments.")
    # Else scourgify
    else:
        scourgify()

def scourgify():
    # Open file and read "name" and "house"
    list = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Split "name" into "first" and "last" and write that and "house" into argv[3]
                last, first = row["name"].split(", ")
                list.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File not readable")
    # Write new file
    with open(sys.argv[2], "w") as newfile:
        writer = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in list:
            writer.writerow(row)


if __name__ == "__main__":
    main()
