class Circle:
    # Private class variable
    __pi = 3.141

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Using the private class variable __pi
        return self.__pi * (self.radius ** 2)

    def circumference(self):
        # Using the private class variable __pi
        return 2 * self.__pi * self.radius

# Example usage:
circle = Circle(5)
print("Area:", circle.area())              
print("Circumference:", circle.circumference()) 
