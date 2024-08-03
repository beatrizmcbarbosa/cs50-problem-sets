class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        
    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"
    
    
def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]
    for package in packages:
        print(package)
if __name__ == "__main__":
    main()