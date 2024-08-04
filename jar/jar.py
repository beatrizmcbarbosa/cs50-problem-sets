class Jar:
    # Initialise cookir jar with capacity
    # If capacity is not a non-negative int, raise ValueError
    def __init__(self, capacity=12):
        ...
    # Return a string with 🍪 * number of cookies in the jar. 3 cookies == 🍪🍪🍪
    def __str__(self):
        ...

    # Add n cookies to the jar. If adding more than capacity, raise ValueError
    def deposit(self, n):
        ...

    # Remove n cookies from the jar. If n is higher than the cookies existing in the jar, raise ValueError
    def withdraw(self, n):
        ...

    # Return jar's capacity
    @property
    def capacity(self):
        ...

    # Return number of cookies in the jar, initially 0
    @property
    def size(self):
        ...
