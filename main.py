import matplotlib.pyplot as plt
import numpy as np
from x_and_y import *

x = np.linspace(0, generate_x_and_y(x=1, y=3))
y = np.linspace(0, generate_x_and_y(x=5, y=8))

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, y, label='line')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Homework")
plt.legend()
plt.show()
