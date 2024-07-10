import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Too many or few command-line arguments")
    elif (sys.argv[1]).endswith(".py") == False:
        sys.exit("Not a python file")
    else:
        print(count_lines())

def count_lines():
    lines = 0
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.lstrip() != "" and (line.lstrip().startswith("#") == False):
                lines += 1
        return lines

if __name__ == "__main__":
    main()