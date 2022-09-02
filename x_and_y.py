import random


def generate_x_and_y(x, y):
    if x < y:
        x, y = x, y
    x_y_list = [x, y]
    for _ in range(2):
        random.randint(1, 20)
    return x_y_list[0], x_y_list[1]
