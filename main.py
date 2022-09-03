import matplotlib.pyplot as plt
from x_and_y import *

for _ in range(4):
    which_plot = input("""Which plot would you like to see?
    Plot numbers: [1, 2, 3]
    Input plot number: """)
    print('=' * 50)
    if which_plot == '1':
        plt.plot(generate_x_and_y(0, 0), label='Line - 1', color='red')
        plt.plot(generate_x_and_y(0, 0), label='Line - 2', color='blue')
        plt.plot(generate_x_and_y(0, 0), label='Line - 3', color='yellow')
        plt.plot(generate_x_and_y(0, 0), label='Line - 4', color='black')
        plt.xlabel('Label - X')
        plt.ylabel('Label - Y')
        plt.title("Homework - Plot 1")
        plt.legend()
        plt.show()
    elif which_plot == '2':
        plt.plot(generate_x_and_y2(0, 0), label='Line - 1', color='red')
        plt.plot(generate_x_and_y2(0, 0), label='Line - 2', color='blue')
        plt.xlabel('Label - X')
        plt.ylabel('Label - Y')
        plt.title("Homework - Plot 2")
        plt.legend()
        plt.show()
    elif which_plot == '3':
        plt.plot(generate_x_and_y3(0, 0), label='Line - 1', color='black')
        plt.xlabel('Label - X')
        plt.ylabel('Label - Y')
        plt.title("Homework - Plot 3")
        plt.legend()
        plt.show()
    else:
        print("Plot doesn't exist.")
        print('=' * 50)
