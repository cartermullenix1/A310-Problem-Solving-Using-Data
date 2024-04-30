import math
from Point import Point
from Line import Line

class Triangle(Line):
    def __init__(self, p1, p2, p3):
        self.l1 = Line(p1,p2)
        self.l2 = Line(p2,p3)
        self.l3 = Line(p3,p1)
    def __str__(self):
        return "Triangle {" + str(self.l1.p1) + ", " + str(self.l2.p1) + ", " + str(self.l3.p1) + "}"
    def area(self):
        x = (self.l1.length() + self.l2.length() + self.l3.length())/2
        a = math.sqrt(x*(x - self.l1.length())*(x - self.l2.length())*(x - self.l3.length()))
        return a

# print("--------------------Test Cases-----------------------")

# a = Point(4,5)
# b = Point(2,2)
# c = Point(5,1)
# tri = Triangle(a,b,c)
# d = tri.area()
# print("Area of ", tri, " is: ", d)