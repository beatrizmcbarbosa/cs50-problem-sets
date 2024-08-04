class Jar:
    # Initialise cookie jar with capacity
    # If capacity is not a non-negative int, raise ValueError
    def __init__(self, capacity=12):
        self.capacity = capacity

    # Return a string with 🍪 * number of cookies in the jar. 3 cookies == 🍪🍪🍪
    def __str__(self):
        return f"🍪"

    # Add n cookies to the jar. If adding more than capacity, raise ValueError
    def deposit(self, n):
        return (self.capacity + n)

    # Remove n cookies from the jar. If n is higher than the cookies existing in the jar, raise ValueError
    def withdraw(self, n):
        return (self.capacity - n)

    # Return jar's capacity
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    # Return number of cookies in the jar, initially 0
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    print(f"{jar}")

if __name__ == "__main__":
    main()

