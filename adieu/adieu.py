names = []

def main():
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            adieu()
            break

def adieu():
    if len(names) == 1:
        print("Adieu, adieu, to " + names[0])
    elif len(names) >= 2:
        mid_names = ", ".join(names[0:-1])
        print("Adieu, adieu, to", mid_names, "and", names[-1])

main()

