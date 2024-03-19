
# Нужно реализовать нейронную сеть из 4 нейронов типа WTA, предназначенных для классификации ->
# -> входных двухкомпонентных векторов
# х - список векторов входных параметров
# n - коэффициент скорости обучения
# w - веса
# out - ответ нейрона (победил/проиграл)
# threshold_number_win - пороговое число побед нейрона (для системы штрафов)
# Я выбрал систему с паузой при достижении порогового числа побед
# Для обучения Нейронов Хебба нужно: рандомизировать коэффициент обучение n(0, 1); ->
# -> изменить метод изменения весов нейронов (сделать по правилу Хебба)

from random import *

class Neuron_WTA:
    w = []
    x = []
    out = 0

    def __init__(self, x_in):
        """Инициализация нейрона (создаём веса и передаём входные параметры)"""
        self.w = [uniform(-1.00, 1.00) for i in range(2)]
        self.x = x_in
    
    def summat(self):
        """Сумматор нейрона (возвращает выходной сигнал)"""
        u = 0
        for i in range(len(self.x)):
            u += self.w[i] * self.x[i]
        return u
    
    def return_w(self):
        """Вспомогательная функция, возвращает массив весов нейрона"""
        return self.w
    
    def save_change_w(self, n, u, x_in):
        """Вспомогательная функция, изменяет веса нейрона (через приращение)"""
        for i in range(len(self.w)):
            self.w[i] += n * x_in[i] * u

class Neural_Network:
    def loop(self, neurons):
        """Прогонка нейронов (1 круг обучения, возвращает массив выходных сигналов)"""
        u = []
        for neuron in neurons:
            u.append(neuron.summat())
        return u
    
    def change_w(self, neurons, n, u, x_in):
        """Изменение весов нейронов по правилу Хебба"""
        for i in range(len(neurons)):
            neurons[i].save_change_w(n, u[i], x_in)
            

x = [[0.97, 0.20], [1.00, 0.00], [-0.72, 0.70], [-0.67, 0.74], [-0.80, 0.60], [0.00, -1.00], 
     [0.20, -0.97], [-0.30, -0.95]]
n = uniform(0.01, 0.99)

for i in range(len(x)):
    print("-" * 50)
    neurons = [Neuron_WTA(x[i]) for j in range(2)]
    print("Стартовые веса нейронов для входного вектора:")
    for neuron in neurons:
        print(f"{neuron.w},   {neuron.x}")
    nn = Neural_Network()
    for l in range(10):
        out_mas = nn.loop(neurons)
        print(f"Выходные сигналы нейронов: {out_mas}")
        nn.change_w(neurons, n, out_mas, x[i])
        print("Изменение весов нейронов:")
        for k in range(len(neurons)):
            print(f"Нейрон {k}: {neurons[k].w}")
        print(f"Это был {l + 1} круг обучения")
