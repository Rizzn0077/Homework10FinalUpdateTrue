import random


def generate_x_and_y(x, y):
    if x < y:
        x, y = x, y
    x_y_list = []
    for _ in range(8):
        num = random.randint(1, 150)
        x_y_list.append(num)
    return x_y_list[0], x_y_list[1], x_y_list[2], x_y_list[3], x_y_list[4], x_y_list[5], x_y_list[6], x_y_list[7]


def generate_x_and_y2(x, y):
    if x < y:
        x, y = x, y
    x_y_list = []
    for _ in range(2):
        num = random.randint(1, 150)
        x_y_list.append(num)
    return x_y_list[0], x_y_list[1]


def generate_x_and_y3(x, y):
    if x < y:
        x, y = x, y
    x_y_list = []
    for _ in range(3):
        num = random.randint(1, 150)
        x_y_list.append(num)
    return x_y_list[0], x_y_list[1], x_y_list[2]
