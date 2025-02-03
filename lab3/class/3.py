class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
print("Площадь Shape:", shape.area())  

length = float(input("Введите длину стороны квадрата: "))
square = Square(length)
print("Площадь квадрата:", square.area())  
