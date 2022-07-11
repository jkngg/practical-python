# bounce.py
#
# Exercise 1.5
height = 100.0
jump_portion = 3/5
counter = 0

while counter <= 9:
    height *= jump_portion
    counter += 1
    print(counter, round(height, ndigits=4))