# bounce.py
#
# Exercise 1.5

height = 100  # in meters
bounce = 3 / 5  # in meters
bounce_count = 1  # initialize bounce count


while bounce_count < 11:
    height = height * bounce  # updating to new height
    print(bounce_count, round(height, 4))  # bounce calculation
    bounce_count += 1  # update bounce count
