import validators

def main():
    userEmail = input("Email: ")
    print(validate(userEmail))

def validate(email):
    if validators.email(email) == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
