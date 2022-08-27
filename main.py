import matplotlib.pyplot as plt
from x_and_y import *

plt.plot(x1, y1, label="Лінія 1")
plt.plot(x2, y2, label="Лінія 2")
plt.plot(x3, y3, label="Лінія 3")
plt.xlabel('Сторона X')
plt.ylabel('Сторона X')
plt.title('Домашня Робота')
plt.legend()
plt.show()
