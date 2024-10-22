
#Метод Ньютона-Рафсона
#Функция: f(x, y) = 8x^2 + y^2 - xy + x; x_0(2; 2); epsilon_1 = 0.1; epsilon_2 = 0.15; m = 10; grad_f(x, y) = (16x - y + 1; 2y - x);
#k = 0; H(x) = [[16, -1], [-1, 2]]
#Вывод: x_min; f(x_min); k; график

import math as mt
import numpy as np
import sympy as sp
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

def f(x_list: list[list[float]]) -> list[list[float]]:
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

def reverse_mat(h: list[list[float]]) -> list[list[float]]:
    """
    Функция, которая вычисляет обратную матрицу
    Args: h - матрица Гиссе
    Return: обратная матрица
    """
    return np.linalg.inv(h)

def calculate_deltas(h: list[list[float]]) -> list[float]:
    """
    Функция, которая вычисляет 2 дельты матрицы
    Args: h - матрица Гиссе
    Return: список из двух дельт
    """
    return [h[0][0], np.linalg.det(h)]

def calculate_d(x: list[float], h_reverse: list[list[float]], f: int) -> list[float]:
    """
    Функция, которая вычисляет вектор d
    Args: x - список значений, h_reverse - матрица Гиссе (уже обратная), f - флаг для выбора варианта вычисления
    Return: список d
    """
    if f == 1:
        return -(np.dot(h_reverse, grad_f(x)))
    elif f == 2:
        return [-x for x in grad_f(x)]
    else:
        print("Выбран неверный флаг! Можно указать 1 или 2")

def calculate_t(x_old: list[float], d: list[float]) -> float:
    """
    Функция, которая вычисляет значение t на какой-то итерации
    Args: x_old - список значений; d - коэффициент d
    Return: значение t
    """
    t = sp.symbols("t")  #объявляем символьную переменную
    expression_x_new = [x_old[0] + t * d[0], x_old[1] + t * d[1]]
    after_f = (8 * (expression_x_new[0]**2)) + (expression_x_new[1]**2) - (expression_x_new[0] * expression_x_new[1]) + expression_x_new[0]
    after_f_derivative = sp.diff(after_f, t)  #берём производную по t
    solution_t = sp.solve(after_f_derivative, t)  #решение уравнения производной = 0 для t
    return solution_t

def calculate_x_new(x_old: list[float], t: float, d: list[float]) -> list[float]:
    """
    Функция, которая вычисляет новое значение вектора x
    Args: x_old - предыдущее значение вектора x; t - коэффициент t; d - коэффициент d
    Return: новый вектор x
    """
    return np.array(x_old) + t * np.array(d)

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
h = [[16, -1], [-1, 2]]
flag = 0

while k < m:
    #шаг 3
    grad_x_0 = grad_f(x_0)
    #шаг 4
    norm_grad_x_0 = norm_grad(grad_x_0)
    if norm_grad_x_0 < epsilon_1:
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
            #шаг 6-7
            h_reverse = reverse_mat(h)
            #шаг 8
            deltas = calculate_deltas(h_reverse)
            if deltas[0] > 0 and deltas[1] > 0:
                d = calculate_d(x_0, h_reverse, 1)
            else:
                d = calculate_d(x_0, h_reverse, 2)
            #шаг 9-10
            t = calculate_t(x_0, d)
            #шаг 11
            x_new = calculate_x_new(x_0, t, d)
            #шаг 12
            between_x = norm_between_x(x_0, x_new)
            between_f = mod_between_f([x_0], [x_new])
            if between_x < epsilon_2 and between_f < epsilon_2:
                if flag == 1:
                    flag = 2
                    x_min = x_new
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
