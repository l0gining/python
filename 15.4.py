from math import *
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

    def set(self, x, y):
        self.x = x
        self.y = y

    def LengthToOrgign(self):
        """Вычисление длины до начала координат"""
        return sqrt((self.x**2)+(self.y**2))

newPoint = Point(5, 3)
print('Координаты точки: {}'.format(newPoint.get()))
newPoint.set(3, 5)
print('Новые координаты точки: {}'.format(newPoint.get()))
print('Длина от точки до начала координат: {}'.format(newPoint.LengthToOrgign()))
