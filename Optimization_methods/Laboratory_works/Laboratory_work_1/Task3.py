
#Нахождение точки min методом Фибоначчи
#Входные данные: сама функция; интервал неопределённости l; точность epsilon; кол-во вычисленных значений n; ->
# -> некоторая const размерности alpha
#Выходные данные: сама функция; точка min; значение функции в точке min; интервал, в котором нашлась ->
# -> точка min; конечный индекс интервала i

import math as mt
import matplotlib.pyplot as plt
import numpy as np

def base_func(x_list):
    """
    Базовая функция из условия
    Args: x_list - список входных значений
    Return: список результатов функции
    """
    result = []
    for i in range(len(x_list)):
        result.append((2 * mt.pow(x_list[i], 2)) - (2 * x_list[i]) + (5 / 2))
    return result

def fibonachchi_func(quantity):
    """
    Функция, которая считает числа Фибоначчи
    Args: quantity - количество чисел, которое нужно найти
    Return: список чисел Фибоначчи
    """
    if quantity == 1:
        return [1]
    elif quantity == 2:
        return [1, 1]
    else:
        result = [1, 1]
        for i in range(quantity):
            if i < 2:
                pass
            else:
                result.append(result[i - 1] + result[i - 2])
        return result

def calculate_lambda_i_mu_i(l, fib_list, i):
    """
    Функция, которая рассчитывает значения lambda_i и mu_i
    Args: l - интервал неопределённости; fib_list - список чисел Фибоначчи; i - индекс итерации
    Return: lambda_i и mu_i
    """
    n = len(fib_list)
    lambda_i = l[0] + ((fib_list[(n - 1) - i - 1] / fib_list[(n - 1) - i + 1]) * (l[1] - l[0]))
    mu_i = l[0] + ((fib_list[(n - 1) - i] / fib_list[(n - 1) - i + 1]) * (l[1] - l[0]))
    return lambda_i, mu_i

def calculate_new_l(lambda_i, mu_i, l):
    """
    Функция, которая переопределяет интервал неопределённости
    Args: lambda_i - текущая lambda_i; mu_i - текущее mu_i; l - интервал неопределённости
    Return: новый интервал неопределённости
    """
    new_l = [0, 0]
    f_lambda_i = base_func([lambda_i])[0]
    f_mu_i = base_func([mu_i])[0]
    if f_lambda_i > f_mu_i:
        new_l[0] = lambda_i
        new_l[1] = l[1]
    else:
        new_l[0] = l[0]
        new_l[1] - mu_i
    return new_l

def calculate_accuracy(l, epsilon):
    """
    Функция, которая рассчитывает точность текущего интервала неопределённости
    Args: l - интервал неопределённости; epsilon - точность
    Return: True (точность достигнута) / False (точность не достигнута)
    """
    f = False
    if mt.fabs(l[1] - l[0]) < epsilon:
        f = True
    return f

l = [-1, 9]  #интервал неопределённости
epsilon = 0.5  #точность
i = 3  #счётчик итераций
n = 10  #кол-во чисел Фибоначчи
alpha = 0.1  #константа

print(f"""
Входные данные:
Функция: 2x^2 - 2x + 5/2
Интервал неопределённости: {l}
Точность: {epsilon}
Кол-во чисел Фибоначчи: {n}
""")

fib_list = fibonachchi_func(n)
while not calculate_accuracy(l, epsilon):
    lambda_i, mu_i = calculate_lambda_i_mu_i(l, fib_list, i)
    l = calculate_new_l(lambda_i, mu_i, l)
    i += 1

print(f"""
Выходные значения:
Функция: 2x^2 - 2x + 5/2
Интервал неопределённости: {l}
Точка минимума: {(l[1] + l[0]) / 2}
Значение функции в точке минимума: {base_func([(l[1] + l[0]) / 2])[0]}
Конечное k: {i}
Конечный индекс интервала неопределённости: {i*2 + 1}
Точность (по отношению к epsilon): {mt.fabs(l[1] - l[0])}
Сходимость: {1 / fib_list[len(fib_list) - 1]}
""")

x_range = np.linspace(-1, 9, 1000)
plt.plot(x_range, base_func(x_range), label="f(x)")
plt.scatter((l[1] - l[0]) / 2, base_func([(l[1] - l[0]) / 2]), color="blue", s=20, label="min")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
