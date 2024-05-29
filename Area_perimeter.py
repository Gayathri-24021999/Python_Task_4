class Circle:
    # Private class variable
    __pi = 3.141

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def area(cls, radius):
        # Using the private class variable __pi
        return cls.__pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        # Using the private class variable __pi
        return 2 * cls.__pi * radius

# Example usage:
radius = 5
print("Area:", Circle.area(radius))            
print("Perimeter:", Circle.perimeter(radius)) 
