import numpy as np
import matplotlib.pyplot as plt

# Создание окна с двумя графиками
x1 = np.linspace(-2, 6, 100)
y1 = x1**2 - 4*x1 + 4  # f(x) = x^2 - 4x + 4
y2 = 2*x1 + 3          # f(x) = 2x + 3

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(x1, y1, label='f(x) = x^2 - 4x + 4', color='green')
plt.title('График функции f(x) = x^2 - 4x + 4')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x1, y2, label='f(x) = 2x + 3', color='orange')
plt.title('График функции f(x) = 2x + 3')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

x2 = np.linspace(-2, 2, 100)
y2 = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x2, y2)
Z = (X**2 + Y**2 - 1)**3 - X**2 * Y**3  # f(x, y)

#Создание окна с одним графиком
plt.figure(2)
plt.contourf(X, Y, Z, levels=50, cmap='red')
plt.colorbar()
plt.title('График функции f(x, y) = (x^2 + y^2 - 1)^3 - x^2y^3')
plt.xlabel('x')
plt.ylabel('y')

plt.show()