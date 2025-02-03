import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты точки: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


x1 = float(input("Введите координату x первой точки: "))
y1 = float(input("Введите координату y первой точки: "))
p1 = Point(x1, y1)


x2 = float(input("Введите координату x второй точки: "))
y2 = float(input("Введите координату y второй точки: "))
p2 = Point(x2, y2)

p1.show()

dx = float(input("Введите изменение по x для перемещения точки: "))
dy = float(input("Введите изменение по y для перемещения точки: "))
p1.move(dx, dy)
print("После перемещения:")
p1.show()

print("Расстояние между точками:", p1.dist(p2))
