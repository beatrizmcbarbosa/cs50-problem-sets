def main():
    greeting=str(input("Greeting: ")).strip()
    print(f'$ {value(greeting)}')

def value(greeting):
    greeting = greeting.lower()
    if greeting=="hello" or greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()