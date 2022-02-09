from typing import Type


class Rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2)**.5

    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                picture += '*' * self.width + '\n'
        return picture

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_amount_inside(self,shape):
        return self.get_area()/shape.get_area()//1

class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(width=side, height=side)

    
    def __str__(self):
        super(Square, self).__str__()
        return f"Square(side={self.height})"

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side):
        self.width = side
        self.height = side

