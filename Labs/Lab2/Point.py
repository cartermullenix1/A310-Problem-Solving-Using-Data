import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def distanceTo(self, other):
        distance = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance

# print("--------------------Test Cases-----------------------")

# a = Point(3,2)
# b = Point(-1,5)
# print(a) # prints: (3,2)
# print("I have two point objects: " + str(a) + " " + str(b))
# # I have two point objects: (3,2) (-1,5)
# howFar = a.distanceTo(b)
# print(howFar) # prints 5

# a = Point(0,0)
# b = Point(1,1)
# print("Distance from " + str(a) + " to" + str(b) + " is: " + str(a.distanceTo(b)))