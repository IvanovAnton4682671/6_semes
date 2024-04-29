
#Метод наискорейшего градиентного спуска
#Функция: f(x) = (8 * (x_1)^2) + (x_2)^2 - (x_1 * x_2) + x_1; x_0 = (2; 2); epsilon_1 = 0.1; epsilon_2 = 0.15; количество итераций M = 10;
#grad_f(x) = (16x_1 - x_2 + 1; 2x_2 - x_1)
#Вывод: точка min; f(min); k; график

import numpy as np
import math as mt
import matplotlib.pyplot as plt

def create_x_range() -> list[list[float]]:
    """
    Функция, которая создаёт диапазон для функции
    Args: отсутствует
    Return: список списков с точками
    """
    x_range = []
    step = 10 / 500
    for i in range(1000):
        x_range.append([-10 + (step * i), -10 + (step * i)])
    return x_range

def f(x_list: list[list[float]]) -> list[float]:
    """
    Функция двух переменных
    Args: x - список значений x
    Return: список значений функции
    """
    result = []
    for x in x_list:
        result.append([(8 * (x[0]**2)) + (x[1]**2) - (x[0] * x[1]) + x[0]])
    return result

def grad_f(x: list[float]) -> list[float]:
    """
    Функция, которая считает градиент функции f
    Args: x - аргумент функции
    Return: список значений
    """
    result = []
    result.append((16 * x[0]) - x[1] + 1)
    result.append((2 * x[1]) - x[0])
    return result

def norm_grad(grad: list[float]) -> float:
    """
    Функция, которая считает норму градиента
    Args: grad - градиент функции
    Return: значение нормы градиента функции
    """
    return mt.sqrt(grad[0]**2 + grad[1]**2)

def calculate_t(x: list[float]) -> float:
    """
    Функция, которая вычисляет значение t на какой-то итерации
    Args: x - аргумент
    Return: значение t
    """
    return ((16 * x[0] * (16 * x[0] - x[1] + 1)) + (2 * x[1] * (2 * x[1] - x[0])) - (x[1] * (16 * x[0] - x[1] + 1)) - (x[0] * (2 * x[1] - x[0])) + (16 * x[0] - x[1] + 1)) / ((-2 * (2 * x[1] - x[0]) * (16 * x[0] - x[1] + 1)) + (2 * (2 * x[1] - x[0])**2) + (16 * (16 * x[0] - x[1] + 1)**2))

def calculate_new_x(x_old: list[float], t: float) -> list[float]:
    """
    Функция, которая вычисляет новое значение х
    Args: x - значение старого x; t - значение t
    Return: новое значение x
    """
    new_x = []
    new_x.append(x_old[0] - t * grad_f(x_old)[0])
    new_x.append(x_old[1] - t * grad_f(x_old)[1])
    return new_x

def norm_between_x(x_old: list[float], x_new: list[float]) -> float:
    """
    Функция, которая вычисляет норму между новым и старым х
    Args: x_old и x_new - старый и новый х
    Return: значение нормы
    """
    return mt.sqrt((x_new[0] - x_old[0])**2 + (x_new[1] - x_old[1])**2)

def mod_between_f(x_old: list[float], x_new: list[float]) -> float:
    """
    Функция, которая вычисляет модуль между разницей новой и старой f
    Args: x_old и x_new - старый и новый х
    Return: значение модуля
    """
    return abs(f(x_new)[0][0] - f(x_old)[0][0])

x_0 = [2, 2]
epsilon_1 = 0.1
epsilon_2 = 0.15
m = 10
k = 0
flag = 0

while k < m:
    #шаг 3
    grad_f_x_0 = grad_f(x_0)
    #шаг 4
    norm_grad_f_x_0 = norm_grad(grad_f_x_0)
    if norm_grad_f_x_0 < epsilon_1:
        x_min = x_0
        f_min = f([x_min])
        break
    else:
        #шаг 5
        if k >= m:
            x_min = x_0
            f_min = f([x_min])
            break
        else:
            #шаг 6
            t = calculate_t(x_0)
            #шаг 7
            x_new = calculate_new_x(x_0, t)
            #шаг 8
            between_x = norm_between_x(x_0, x_new)
            between_f = mod_between_f([x_0], [x_new])
            if between_x < epsilon_2 and between_f < epsilon_2:
                if flag == 1:
                    flag = 2
                    x_min = x_0
                    f_min = f([x_min])
                    break
                else:
                    flag = 1
                    x_0 = x_new
                    k += 1
            else:
                x_0 = x_new
                k += 1

print(f"x_min: {x_min}; f(x_min): {f_min}; k: {k}")

x_range = create_x_range()
tmp_x1 = [x_range[i][0] for i in range(len(x_range))]
tmp_x2 = tmp_x1.copy()
#создаём сетку значений для построение поверхности
x, y = np.meshgrid(tmp_x1, tmp_x2)
#превращение массива от функции f в массив numpy (нужно для lot_surface)
z = np.array(f(x_range))
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")
ax.plot_surface(x, y, z)
ax.scatter(x_min[0], x_min[1], f_min, color="red")
plt.show()
