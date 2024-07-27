# Greeting
name = input("What's your name? ").strip()

# Condition for response
if len(name) <= 3:
    print("Name too short")
else:
    print("Hello,", name)