
# План, что и как будем делать
# Создаём нейронку, в которой 1 нейрон
# Создаём случайные веса нейронам
# Выбираем функцию, которую будем минимизировать в процессе обучения. Возьмём среднеквадратичную ошибку
# Обучаем нейронку на предоставленных точках и сравниваем с желаемым выходом (классы 1 и 0)
# Применяем функцию ReLU к выходу нейрона
# Проверяем, как наша нейронка разделяет точки
# p - входные точки
# y - верные ответы (класс 1 для 1 и 2 точки, 0 - для 3 и 4)
# n - скорость обучения
# e - кол-во эпох обучения

from random import *
import math

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

# По сути, у нас имеется по 2 примера на каждый желаемый выходной сигнал
p = [[0, 0], [1, 1], [1, 0], [0, 1]]
y = [1, 1, 0, 0]
n = 0.3
e = 1000

neural_network = Neural_Network()
neuron = Neuron()

print("Классификация точек до обучения:")
for i in range(len(p)):
    neuron_out = neural_network.relu(neuron.summat(p[i]))
    class_p = 0 if neuron_out < 0.5 else 1
    print(f"Точке {p[i]} присвоен класс {class_p}")

for i in range(e):
    errors = []
    neuron_outs = []
    for j in range(len(p)):
        neuron_out = neural_network.relu(neuron.summat(p[j]))
        neuron_outs.append(neuron_out)
        error = neural_network.mse_less([y[j]], [neuron_out])  # Передаём данные в виде списков
        errors.append(error)
    gradient = []
    for k in range(len(y)):
        gradient.append(neuron_outs[k] - y[k])
    neuron.change_w(n, y, gradient)
    print(f"Эпоха обучения: {i + 1}/{e}, Ошибка: {errors}")  # Мы получаем ошибки 1.0 и 0.0 из-за функции ReLU

print("Классификация точек после обучения:")
for i in range(len(p)):
    neuron_out = neural_network.relu(neuron.summat(p[i]))
    class_p = 0 if neuron_out < 0.5 else 1
    print(f"Точке {p[i]} присвоен класс {class_p}")
