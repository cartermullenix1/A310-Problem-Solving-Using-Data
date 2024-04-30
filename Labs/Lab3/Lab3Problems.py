# Problem 1

def ProveEquiv(a,b):
    return not (a and b) == (not a) or (not b)

print("---------------------Test Cases-----------------------")

print(ProveEquiv(0,1))
print(ProveEquiv(1,1))
print(ProveEquiv(1,0))
print(ProveEquiv(0,0))

#  Problem 2
"""

not ((not a) or (not b))
not (not a and not b)
a and b"

"""
#  Problem 3

def GradeConvert(grade):
    if grade > 4:
        return "The number is too big"
    elif grade > 3.85:
        return "A"
    elif grade > 3.5:
        return "A-"
    elif grade > 3.15:
        return "B+"
    elif grade > 2.85:
        return "B"
    elif grade > 2.5:
        return "B-"
    elif grade > 2.15:
        return "C+"
    elif grade > 1.85:
        return "C"
    elif grade > 1.5:
        return "C-"
    elif grade > 1.15:
        return "D+"
    elif grade > 0.85:
        return "D"
    elif grade > 0.5:
        return "D-"
    elif grade > 0:
        return "F"
    else:
        return "Invalid Grade"

print("---------------------Test Cases-----------------------")

print(GradeConvert(3.9))
print(GradeConvert(2.65))
print(GradeConvert(1.35))

# Problem 4

class Leap:
    def is_leap_year(year):
        if year < 1582:
            return year % 4 == 0
        else:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

print("---------------------Test Cases-----------------------")

print(Leap.is_leap_year(1992))


# Problem 5

import math

def print_scalable_four(size):
    for row in range(size):
      for col in range(size):
        if row == size//2 or col == size//2 or (row <= size//2 and col == size - size//2- row):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
      print()

print_scalable_four(8)

# Problem 6

size = 5

m = {}
m["width"] = size
m["height"] = size

def show(m):
    for row in range(m["height"]):
        for col in range(m["width"]):
            if (row, col) in m:
                print(m[row, col], end=" ")
            else:
                print(0, end=" ")
        print()
    print("-----------------------------------")

row = size-1
col= size//2
for n in range(1,size*size+1):
    m[row, col] = n
    nurow = (row + 1) % size
    nucol = (col + 1) % size
    if (nurow, nucol) in m:
        row = row -1
        col = col
    else:
        row = nurow
        col = nucol
show(m)