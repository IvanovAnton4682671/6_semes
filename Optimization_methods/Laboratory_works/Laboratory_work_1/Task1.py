
# Нахождение точки минимума методом дихотомии
# Входные данные: интервал неопределённости l; шаг betta; точность epsilon; сама функция; кол-во кругов k
# Выходные данные: исходная функция; точка минимума; интервал, в котором найдена функция; ->
# -> значение функции в точке минимума; n - индекс конечного интервала неопределённости; r - сходимость

import math
import matplotlib.pyplot as plt
import numpy as np

def function(x):
    """Функция, которая считает значение основной функции из условия"""
    res = []
    for i in range(len(x)):
        res.append((2 * math.pow(x[i], 2)) - (2 * x[i]) + (5 / 2))
    return res

def y_z(a, b):
    """Функция, которая находит новые значения y и z"""
    y_new = (a + b - betta) / 2
    z_new = (a + b + betta) / 2
    return y_new, z_new

def fy_fz(y, z):
    """Функция, которая считает значение основной функции в точках y и z"""
    f_y = function([y])
    f_z = function([z])
    if f_y <= f_z:
        l[1] = z
    else:
        l[0] = y
    return 2 * (k + 1)

def accuracy(a, b):
    """Функция, которая проверяет точность"""
    f = False
    if math.fabs(b - a) < epsilon:
        f = True
    return f

l = [-1, 9]
betta = 0.2
epsilon = 0.5
k = 0
n = 0

print()
print(f"""Входные данные:
Интервал неопределённости: {l}
Шаг betta: {betta}
Точность epsilon: {epsilon}
Сама функция: 2x^2 - 2x + 5/2
Начальное k: {k}
      """)

while not accuracy(l[0], l[1]):
    y, z = y_z(l[0], l[1])
    n = fy_fz(y, z)
    accuracy(l[0], l[1])
    k += 1

print(f"""Выходные данные:
Исходная функция: 2x^2 - 2x + 5/2
Точка минимума: {(l[1] + l[0]) / 2}
Конечный интервал неопределённости: {l}
Значение функции в точке минимума: {function([(l[1] + l[0]) / 2])}
Индекс конечного интервала неопределённости: {n}
Сходимость: {1 / (math.pow(2, n))}
Конечное к: {k}
Точность (по отношению к epsilon): {math.fabs(l[1] - l[0])}
      """)

x_range = np.linspace(-1, 9 ,1000)
plt.plot(x_range, function(x_range), label='f(x)')
plt.scatter((l[1] + l[0]) / 2, function([(l[1] + l[0]) / 2]), color='blue', s=20, label='Минимум')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
