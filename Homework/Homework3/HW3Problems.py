# Problem 1

# What does round(...) return when applied to ±2.1, ±2.9? (Four cases).

(a,b) = (2.1, 2.9)

assert (round(a), round(b)) == (2, 3), "test 01.a failed"
assert (round(-a), round(-b)) == (-2, -3), "test 01.b failed"

# Problem 2

# Same question but this time as it applies to int(...). Use assert to test.

(a,b) = (2.1, 2.9)

assert (int(a), int(b)) == (2, 2), "test 02.a failed"
assert (int(-a), int(-b)) == (-2, -2), "test 02.b failed"

# Problem 3

# Evaluate: list(range(12, 16)), list(range(0, 10, 2)), and list(range(5, -1, -1)).

assert (list(range(12,16)) == [12,13,14,15]), "test 03.a failed"
assert (list(range(0,10,2)) == [0,2,4,6,8]), "test 03.b failed"
assert (list(range(5,-1,-1)) == [5,4,3,2,1,0]), "test 03.c failed"

# Problem 4

# Write an assert for each one of: random.randint(1, 10), random.randint(1, 2)

import random

assert 1 <= random.randint(1,10) <= 10, "test 04.a failed"
assert random.randint(1,2) in [1,2], "test 04.a failed"

# Problem 5

# Consider the function defintion below, write an assertion for what(10):

def what(n): # n > 0
    if n == 1: return 1
    else: return n + what(n-1)

assert what(10) == 55, "test 05 failed"

# Problem 6

# Consider the function definition below, please write an assertion for what(-5, 3):

def what(n, m):
    if n < 0:
        return -what(-n, m)
    else:
        if n == 1:
            return m
        else:
            return m + what(n-1, m)

assert what(-5, 3) == -what(5,3), "False"
assert what(5, 3) == 15, "test 06 failed"

# Problem 7

# Consider the function definition below, please write an assertion for:

def what():
  pass

assert what() == None, "test 07 failed"

# Problem 8

# Given a = [3, 1, 5, 6, 4, 2] write an assertion for random.choice(a)

a = [3,1,5,6,4,2]

assert random.choice(a) in a, "test 08 failed"

# Problem 9

# For the same list a above write an assertion for random.shuffle(a)

a = [3,1,5,6,4,2]
b = sorted(a)
random.shuffle(a)
assert(sorted(a) == sorted(b)), "test 09 failed"

# Problem 10

# What happens when you run this code:

try:
  print(1 + 'a')
except:
  print('1a');

# The function will print '1a'

# Problem 11

# Solve the Coin Flip Streaks problem on page 107 in your Sweigart text

StreakNumber = 0
Sample_Space = ['H', 'T']
for experiment in range(10000):
  flips = ''
  for i in range(100):
    flips += random.choice(Sample_Space)
    
    count = 1
    for i in range(1,len(flips),1):
      if flips[i] == flips[i-1]:
        count += 1
        if count == 6:
          StreakNumber += 1
          break
      else:
        count = 1
print('Chance of streak: %s%%' % (StreakNumber / 100))

#Problem 12

# Create a matrix of numbers like in Lab 03 using a dictionary for data representation

matrix = {}
matrix[0,0] = 1
matrix[1,0] = -2
matrix[0,1] = 3
matrix[1,1] = 8
print(matrix)


# Problem 13

# Give examples in code for escape characters, raw strings, multiline strings and comments

# Escaped Characters
print('I can\'t see')

# Raw Strings
print(r'I can\'t see you')

# Multiline Strings

print('''Dear Professor G,
      
      I will not be able to make it to class today.
      What do I need to do to catch up
      
      Thanks,
      Carter
      ''')

# Problem 14

# Give examples in code for three useful isX() methods, join() and split()

# isX() Methods
print('Hi my name is Carter'.istitle())
print('Hi my name is Carter'.isalpha())
print('Hi my name is Carter'.isalnum())

# join() Method
print(' '.join(['Hi', 'my', 'name', 'is', 'Carter']))

# split() Method
print('Hi my name is Carter'.split(' '))

# Problem 15

# Give examples in code for how to justify text, remove whitespace and use ord() and chr() functions

# Justifying Text
print('Carter'.rjust(10))
print('Carter'.ljust(10, '*'))

# Removing Whitespace
print('XXXXXCarterXXXXX'.strip('X'))
print('XXXXXCarterXXXXX'.rstrip('X'))
print('XXXXXCarterXXXXX'.lstrip('X'))

# ord() and chr()
print(ord('B'))
print(chr(66))
print((chr(66)) == 'B' and ord('B') == 66)