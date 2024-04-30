import random
from random import choice

n = 75

def flip(n):
    scount = 0
    for i in range(n):
        a_flip = random.choice(['H', 'T'])
        if scount == 0:
            scount = 1
            previous = a_flip
        elif a_flip == previous:
            scount = scount + 1
            if scount == 6:
                return 1
            else:
                previous = a_flip
        else:
            scount = 1
            previous = a_flip
    return 0


trials = 100
sum = 0
for i in range(trials):
    sum = sum + flip(n)

print(sum / trials)
    
