#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
msg = "Last digit of {} is {} and is {}"
if number < 0:
    last_digit *= -1
if (last_digit == 0):
    print(msg.format(number, last_digit, "0"))
elif (last_digit > 5):
    print(msg.format(number, last_digit, "greater than 5"))
elif (last_digit < 6):
    print(msg.format(number, last_digit, "less than 6 and not 0"))
