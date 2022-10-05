class Point:
    def __init__(self, x, y):
        self.x = x
        self.x = x


class Rectangle:
    def __init__(self, origin , width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height

    def print_coordinates(self):
        top_right_point = self.origin.x + self.width
        bottom_left_point = self.origin.y + self.height
        print('Starting Point (X)): ' + str(self.origin.x))
        print('Starting Point (Y)): ' + str(self.origin.y))
        print('End Point X-Axis (Top Right): ' + str(top_right_point))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left_point))


def build_rectangle():
    origin = Point(50, 100)
    rectangle = Rectangle(origin, 90, 10)

    return rectangle

rectangle = build_rectangle() 

print(rectangle.compute_area())
rectangle.print_coordinates()
