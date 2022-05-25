from math import cos, sin, radians

class Vec:
    def __init__(self, x, y):
            self.x = x
            self.y = y
    
    def rotate(self, deg):
        rad = radians(deg)
        x = self.x * cos(rad) - self.y * sin(rad)
        y = self.x * sin(rad) + self.y * cos(rad)
        return Vec(x, y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vec(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vec(x, y)

    def __mul__(self, other: int):
        x = self.x * other
        y = self.y * other
        return Vec(x, y)

    def __truediv__(self, other: int):
        x = self.x / other
        y = self.y / other
        return Vec(x, y)

    def __str__(self):
        return f'(x: {self.x} , y: {self.y})'
