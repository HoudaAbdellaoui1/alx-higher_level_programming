#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    string = " is positive"
elif number == 0:
    string = " is zero"
elif number < 0:
    string = " is negative"
print(f"{number}" + string)
