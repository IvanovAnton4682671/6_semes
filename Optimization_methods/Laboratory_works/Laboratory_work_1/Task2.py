
#Нахождение точки min методом золотого сечения
#Входные данные: сама функция; интервал неопределённости l; точность epsilon; начальное k
#Выходные данные: исходная функция; точка min; значение функции в точке min; интервал, в котором ->
# -> находится точка min; индекс конечного интервала n; сходимость r

import math as mt
import matplotlib.pyplot as plt
import numpy as np

def function(x):
    """Функция, которая считает значение основной функции"""
    res = []
    for i in range(len(x)):
        res.append((2 * mt.pow(x[i], 2)) - (2 * x[i]) + (5 / 2))
    return res

def y_z():
    """Функция, которая находит новые значения y и z"""
    y = l[0] + num_1 * (l[1] - l[0])
    z = l[0] + l[1] - y
    return y, z

def fy_fz(y, z, count_n_for, n):
    """Функция, которая считает значение функции в точках y и z"""
    fy = function([y])
    fz = function([z])
    if fy <= fz:
        l[1] = z
        y_new = l[0] + l[1] - y
        z_new = y
    else:
        l[0] = y
        y_new = z
        z_new = l[0] + l[1] - z
    if count_n_for == 0:
        n = 2 * (k + 1)
        count_n_for += 1
    else:
        n += 1
        count_n_for += 1
    return y_new, z_new, count_n_for, n

def accuracy():
    """Функция, которая проверяет точность"""
    f = False
    if mt.fabs(l[1] - l[0]) < epsilon:
        f = True
    return f


num_1 = (3 - mt.sqrt(5)) / 2
num_2 = 1 - num_1
l = [-1, 9]
epsilon = 0.5
k = 0
count_n_for_l = 0
n = 0

print()
print(f"""
Входные данные:
Интервал неопределённости l = {l}
Точность epsilon = {epsilon}
Сама функция: 2x^2 - 2x + 5/2
Начальное k: {k}
""")

y, z = y_z()
while not accuracy():
    y, z, count_n_for_l, n = fy_fz(y, z, count_n_for_l, n)
    k += 1

print()
print(f"""
Выходные данные:
Исходная функция: 2x^2 - 2x + 5/2
Точка min = {(l[1] + l[0]) / 2}
Значение функции в точке min = {function([(l[1] + l[0]) / 2])}
Интервал, в котором находится точка min: {l}
Индекс конечного интервала n = {n}
Сходимость = {mt.pow(num_2, n - 1)}
Конечное k = {k}
Точность (по отношению к epsilon) = {mt.fabs(l[1] - l[0])}
""")

x_range = np.linspace(-1, 9 ,1000)
plt.plot(x_range, function(x_range), label='f(x)')
plt.scatter((l[1] + l[0]) / 2, function([(l[1] + l[0]) / 2]), color='blue', s=20, label='Минимум')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
