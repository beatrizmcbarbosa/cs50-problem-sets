class Jar:
    # Initialise cookie jar with capacity
    # If capacity is not a non-negative int, raise ValueError
    def __init__(self, capacity=12):
        if not capacity > 0:
            raise ValueError("Capacity not valid")
        self.capacity = capacity
        self._size = 0

    # Return a string with 🍪 * number of cookies in the jar. 3 cookies == 🍪🍪🍪
    def __str__(self):
        return f"🍪" * self.size

    # Add n cookies to the jar. If adding more than capacity, raise ValueError
    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Too many cookies")
        self.size += n

    # Remove n cookies from the jar. If n is higher than the cookies existing in the jar, raise ValueError
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("There are not enough cookies")
        self.size -= n

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
        if size <= self._capacity:
            self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
