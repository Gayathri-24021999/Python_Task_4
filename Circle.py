class Circle:
    #Constructor
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159

    def area(self):
        return [self.pi * r ** 2 for r in self.radius]

    def circumference(self):
        return [2 * self.pi * r for r in self.radius]

# Example usage
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)

print("radius:", circle.radius)
print("Areas:", circle.area())
print("Circumferences:", circle.circumference())
