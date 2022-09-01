import matplotlib.pyplot as plt
from x_and_y import *

plt.plot(x_var(), y_var(), label="Лінія 1")
plt.plot(x_var2(), y_var2(), label="Лінія 2")
plt.plot(x_var3(), y_var3(), label="Лінія 3")
plt.plot(x_var4(), y_var4(), label="Лінія 4")
plt.xlabel('Сторона X')
plt.ylabel('Сторона X')
plt.title('Домашня Робота')
plt.legend()
plt.show()
