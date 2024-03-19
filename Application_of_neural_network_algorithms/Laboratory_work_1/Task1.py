
# Нужно реализовать нейронную сеть из 4 нейронов типа WTA, предназначенных для классификации ->
# -> входных двухкомпонентных векторов
# х - список векторов входных параметров
# n - коэффициент скорости обучения
# w - веса
# out - ответ нейрона (победил/проиграл)

from random import *

class Neuron_WTA:
    w = []
    x = []
    out = 0
    kol_win = 0

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
    
    def change_w(self, n):
        """Изменение весов нейрона-победителя по правилу Гроссберга"""
        for i in range(len(self.w)):
            self.w[i] = self.w[i] + n * (self.x[i] - self.w[i])
        self.out = 1
        self.kol_win += 1

class Neural_Network:
    def loop(self, neurons):
        """Прогонка нейронов (1 круг обучения, возвращает массив выходных сигналов)"""
        u = []
        for neuron in neurons:
            u.append(neuron.summat())
        return u
    
    def definition(self, u):
        """Определение нейрона-победителя на кругу обучения (возвращает номер нейрона)"""
        return u.index(max(u))

x = [[0.97, 0.20], [1.00, 0.00], [-0.72, 0.70], [-0.67, 0.74], [-0.80, 0.60], [0.00, -1.00], 
     [0.20, -0.97], [-0.30, -0.95]]
n = 0.5

for i in range(len(x)):
    print("-" * 50)
    neurons = [Neuron_WTA(x[i]) for j in range(4)]
    print("Стартовые веса нейронов для входного вектора:")
    for neuron in neurons:
        print(f"{neuron.w},   {neuron.x}")
    nn = Neural_Network()
    for l in range(10):
        out_mas = nn.loop(neurons)
        print(f"Выходные сигналы нейронов: {out_mas}")
        ind_win = nn.definition(out_mas)
        print(f"Индекс нейрона-победителя: {ind_win}")
        neurons[ind_win].change_w(n)
        print(f"Изменённые веса нейрона-победителя: {neurons[ind_win].w}")
        print("Кол-во побед каждого нейрона:")
        for k in range(len(neurons)):
            print(f"Нейрон {k}, побед: {neurons[k].kol_win}")
        print(f"Это был {l + 1} круг обучения")
