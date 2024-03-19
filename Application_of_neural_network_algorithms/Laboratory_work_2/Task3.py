
# Так так, что тут у нас? Нейросеть, которая должна распознавать буквы X, Y, I, L в виде матриц 3х3
# Задачка как та, которую мы на C# семестр делали, но там да, там была матрица 3х5, да и цифр было аж 10
# Ладно, план действий
# Будем делать сеть из 4 нейронов, то есть буквам будут следующие желаемые выходы: ->
# -> X - 0001, Y - 0010, I - 0100, L - 1000, то есть комбинация ответов нейронов должна выдавать одну букву
# Обучаем на данных 4 буквах, затем тестируем с добавлением шума и смотрим, что по чём
# Возьмём нейроны как из прошлой задачи, функцию ReLU, подгонку весов через градиент
# n - скорость обучения
# e - кол-во эпох обучения
# x - массив букв
# y - желаемые выходы по буквам

import random
import math

class Neuron:
    w = []

    def __init__(self):
        """Создание весов нейрона"""
        self.w = [random.uniform(-1, 1) for i in range(9)]

    def summat(self, x_in):
        """Сумматор нейрона"""
        return 1 + sum([(self.w[i] * x_in[i]) for i in range(len(self.w))])

    def change_w(self, n, x_in, error):
        """Изменение весов методом градиентного спуска"""
        # самая большая сложность оказалась тут
        # суть в том, что веса изменяются на приращение, где приращение - n_in * p(w), ->
        # -> где p(w) - частная производная e/w_ij со знаком минус, где e - 1/2 * sum((y_in - u_in)^2)
        # P.S. Взято из книги Солдатовой О.П. "Нейроинформатика"
        self.w = [w + n * error * x for w, x in zip(self.w, x_in)]

class Neural_Network:
    def relu(self, u_in):
        """Функция активации ReLU"""
        return max(0, u_in)
        #return 1 / (1 + math.exp(-u_in))

    def mse_less(self, y_in, u_in):
        """Функция среднеквадратичной ошибки"""
        #  тут возникает ошибка слишком большого числа, возможно, из-за функции ReLU
        #return (1 / len(y_in)) * sum([math.pow((y_in[i] - u_in[i]), 2) for i in range(len(u_in))])
        return (1 / len(y_in)) * sum([(y_in[i] - u_in[i]) for i in range(len(u_in))])

def test(x_in):
    for i in range(len(x_in)):
        neurons_out = []
        for j in range(len(neurons)):
            neuron_out = neural_network.relu(neurons[j].summat(x_in[i]))
            answer = 0 if neuron_out < 0.5 else 1
            neurons_out.append(answer)
        print(f"Для {i + 1}-ой буквы ответ: {neurons_out}")

neural_network = Neural_Network()
neurons = [Neuron() for i in range(4)]

n = 0.3
e = 1000
x = [[1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 0, 1, 0],
     [0, 1, 0, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 1, 1]]
y = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]

# --------------------Обучение--------------------
for i in range(e):  # цикл по эпохам
    for j in range(len(x)):  # цикл по примерам
        neurons_out = []
        for k in range(len(neurons)):  # цикл по нейронам
            neuron_out = neural_network.relu(neurons[k].summat(x[j]))
            neurons_out.append(neuron_out)
        error = neural_network.mse_less(y[j], neurons_out)
        for k in range(len(neurons)):
            neurons[k].change_w(n, x[j], error)
    if i % 50 == 0:
        print(f"Эпоха обучения: {i}/{e}, ошибка: {error}")

# --------------------Проверка на обычных буквах--------------------
print()
print("--------------------Проверка на обычных буквах--------------------")
test(x)

# --------------------Проверка на <шумных> буквах--------------------
print()
print("--------------------Проверка на <шумных> буквах--------------------")
x_new = [[1, 1, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 1, 0],
         [0, 1, 0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 1, 0]]
test(x_new)
