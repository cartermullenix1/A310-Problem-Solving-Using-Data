from Point import Point

class Line(Point):
    def __init__(self, p1, p2):
        # super().__init__(p1, p2)
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return "(" + str(self.p1) + ", " + str(self.p2) + ")"
    def length(self):
        a = self.p2.distanceTo(self.p1)
        return a

# print("--------------------Test Cases-----------------------")

# a = Point(3,2)
# b = Point(-1,7)
# c = Line(a,b)
# distance = c.length()
# print("Length of Line", c, " is: ", distance)