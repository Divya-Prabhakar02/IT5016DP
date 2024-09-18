class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width* self.height
    def perimeter(self):
        return 2*(self.width+self.height)
rect = Rectangle(4,5)
print(f"Area of Rectangle is {rect.area()}")
print(f"Perimeter of Rectangle is {rect.perimeter()}")


