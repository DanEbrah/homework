import math
from math import pi # circ


class Shape():
    def area():
        pass

class Triangle(Shape):
    def __init__(self, a ,b ,c):
        self.a = a
        self.b = b
        self.c = c
    
    def Tri_area(self, s):
        self.s = s
        s = (self.a + self.b + self.c) /2
        triangle_area = (s*(s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

        assert self.a + self.b > self.c
        assert self.b + self.c > self.a
        assert self.c + self.a > self.b
        
        return triangle_area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def Circ_area(self, area):
        area = pi * self.radius ** 2
        return area

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def Rect_area(self, area):
        area = self.width * self.height
        return area

class Square(Shape):
    def __init__(self, s_h):
        self.s_h = s_h

    def Square_area(self, area):
        area = self.s_h * self.s_h
        return area


tri = Triangle(3, 4, 5)
print(tri.__dict__)
print(f"Area of Triangle is: {tri.Tri_area(tri)}")

print("\n")

circ = Circle(3)
circ.Circ_area(circ)
print(circ.__dict__)
print(f"Area of circle is: {circ.Circ_area(circ)}")

print("\n")

rect = Rectangle(6, 7)
rect.Rect_area(rect)
print(rect.__dict__)
print(f"Area of rectangle is: {rect.Rect_area(rect)}")

print("\n")

square = Square(5)
square.Square_area(square)
print(square.__dict__)
print(f"Area of square is: {square.Square_area(square)}")
