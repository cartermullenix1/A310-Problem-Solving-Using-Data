import math

def richie(number):
    return math.sqrt(number)


print(richie(6))

number = 6

low = 1

high = number
while True:
    guess = (low + high) / 2
    if abs(guess * guess - number) <= 0.0000001:
        print(guess)
        break
    else:
        if guess * guess < number:
            low = guess
        else:
            high = guess