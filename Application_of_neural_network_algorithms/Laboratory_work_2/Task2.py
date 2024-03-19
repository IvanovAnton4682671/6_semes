
# Имеется двухмерный набор данных, то есть как и раньше, 2 веса для двухкомпонентных точек
# Определяем принадлежность к классу так: x1 > x2 -> 1, x1 < x2 -> -1
# Есть какая-то гиперплоскость (линия, уравнение которой: x1 - x2 = 0)
# Единичный квадрат - квадрат со стороной = 1, центрированный относительно начала координат ->
# -> положительный квадрант такого квадрата - область по Х и по У [0, 0.5]
# Для точек сделать метку о принадлежности к классу
# А) Обучаем на 20 точках -> тестируем на 1000 точках (по всему квадрату)
# Б) Сделать то же самое, но с нейроном типа адалайна (адаптивный линейный элемент) (какой-то дискретный случай)
# points_base - обучающие точки
# array_points_base - список, который содержит только пары координат точек
# array_answer - массив желаемых выходов по обучаемым точкам
# n - скорость обучения
# e - кол-во эпох обучения
# points_new - тестируемые точки
# Краткий вывод: нейрон типа адалайна показал лучшую точность. Возможно, из-за линейной функции активации

from random import *
import math

class Point:
    x = []
    class_p = 0

    def __init__(self, digit1, digit2, flag):
        """Создаём точку в заданной области"""
        self.x = [uniform(digit1, digit2) for i in range(2)]
        if flag: self.class_p = 1 if self.x[0] > self.x[1] else (-1)
        else: pass

    def show(self):
        """Вспомогательная функция"""
        print(f"x1 = {self.x[0]}, x2 = {self.x[1]}, class_p = {self.class_p}")

class Neuron:
    w = []

    def __init__(self):
        """Создаём нейрону веса"""
        self.w = [uniform(-1, 1) for i in range(2)]

    def summat(self, x_in):
        """Сумматор нейрона (включая порог)"""
        u = 1  # не забываем про порог
        for i in range(len(self.w)):
            u += self.w[i] * x_in[i]
        return u

    def change_w(self, n, y, gradient):
        """Изменение весов нейрона в зависимости от выхода (градиентный спуск)"""
        self.w[0] -= n * sum([(y[i] + gradient[i]) * (1 + gradient[i]) for i in range(len(y)) if y[i] == 0])
        self.w[1] -= n * sum([(y[i] + gradient[i]) * (1 + gradient[i]) for i in range(len(y)) if y[i] == 1])

class Neuron_Adaline:
    w = []

    def __init__(self):
        """Создаём нейрону веса"""
        self.w = [uniform(-1, 1) for i in range(2)]

    def summat(self, x_in):
        """Сумматор нейрона (включая порог)"""
        u = 1  # не забываем про порог
        for i in range(len(self.w)):
            u += self.w[i] * x_in[i]
        return u

    def activation(self, u):
        """Функция активации - линейная функция"""
        return u

    def change_w(self, n, y, u, x_in):
        """Изменение весов нейрона в зависимости от выхода (не градиентный спуск)"""
        for i in range(len(self.w)):
            self.w[i] -= n * (u - y) * x_in[i]

class Neural_Network:
    def relu(self, u):
        """Функция активации ReLU"""
        return max(0, u)

    def mse_less(self, y, u):
        """Функция среднеквадратичной ошибки"""
        error = 0
        for i in range(len(y)):
            error += math.pow(y[i] - u[i], 2)
        return error / len(y)

points_base = [Point(0, 0.5, True) for i in range(20)]
array_points_base = [[points_base[i].x[0], points_base[i].x[1]] for i in range(len(points_base))]
array_answer = [points_base[i].class_p for i in range(len(points_base))]
n = 0.3
e = 1000

print("--------------------Пункт А--------------------")
neural_network = Neural_Network()
neuron = Neuron()

for i in range(e):
    errors = []
    neuron_outs = []
    for j in range(len(array_points_base)):
        neuron_out = neural_network.relu(neuron.summat(array_points_base[j]))
        neuron_outs.append(neuron_out)
        error = neural_network.mse_less([array_answer[j]], [neuron_out])  # Передаём данные в виде списков
        errors.append(error)
    gradient = []
    for k in range(len(array_answer)):
        gradient.append(neuron_outs[k] - array_answer[k])
    neuron.change_w(n, array_answer, gradient)
    if i % 50 == 0:
        print(f"Эпоха обучения: {i}/{e}, Ошибка: {errors}")  # Мы получаем ошибки 1.0 и 0.0 из-за функции ReLU

print()
points_new = [Point((-0.5), 0.5, True) for i in range(1000)]
array_points_new = [[points_new[i].x[0], points_new[i].x[1]] for i in range(len(points_new))]
print("Классификация точек после обучения:")
kol = 0
for i in range(len(points_new)):
    neuron_out = neural_network.relu(neuron.summat(array_points_new[i]))
    class_p = (-1) if neuron_out < 0.5 else 1
    if i % 50 == 0:
        print(f"Точке {i} присвоен класс {class_p}")
        print(f"Информация самой точки: x1 = {points_new[i].x[0]}, x2 = {points_new[i].x[1]}, class_p = {points_new[i].class_p}")
    if class_p == points_new[i].class_p:
        kol += 1
print(f"Итоговая точность: {kol}/1000")

print()
print("--------------------Пункт Б--------------------")
neural_network = Neural_Network()
neuron = Neuron_Adaline()

for i in range(e):
    errors = []
    neuron_outs = []
    for j in range(len(array_points_base)):
        neuron_out = neuron.activation(neuron.summat(array_points_base[j]))
        neuron_outs.append(neuron_out)
        error = neural_network.mse_less([array_answer[j]], [neuron_out])  # Передаём данные в виде списков
        errors.append(error)
        neuron.change_w(n, array_answer[j], neuron_out, array_points_base[j])
    if i % 50 == 0:
        print(f"Эпоха обучения: {i}/{e}, Ошибка: {errors}")

print()
print("Классификация точек после обучения:")
kol = 0
for i in range(len(points_new)):
    neuron_out = neuron.activation(neuron.summat(array_points_new[i]))
    class_p = (-1) if neuron_out < 0.5 else 1
    if i % 50 == 0:
        print(f"Точке {i} присвоен класс {class_p}")
        print(f"Информация самой точки: x1 = {points_new[i].x[0]}, x2 = {points_new[i].x[1]}, class_p = {points_new[i].class_p}")
    if class_p == points_new[i].class_p:
        kol += 1
print(f"Итоговая точность: {kol}/1000")
