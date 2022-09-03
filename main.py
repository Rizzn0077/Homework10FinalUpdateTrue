import matplotlib.pyplot as plt
from x_and_y import *
x = int(input('Input X: '))
y = int(input('Input Y: '))
color_input = input('Input Color HEX Code / Color Name: ')

plt.plot(generate_x_and_y(x, y), label='Line - 1', color=color_input)
plt.xlabel('Label - X')
plt.ylabel('Label - Y')
plt.title("Homework")
plt.legend()
plt.show()
