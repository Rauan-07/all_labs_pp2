class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
      
        self.length = length
        self.width = width

    def area(self):
        
        return self.length * self.width

shape = Shape()
print("Площадь Shape:", shape.area())  

length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))
rectangle = Rectangle(length, width)
print("Площадь прямоугольника:", rectangle.area())  
 
