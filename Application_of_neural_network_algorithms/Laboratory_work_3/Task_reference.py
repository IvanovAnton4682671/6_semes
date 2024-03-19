
from math import exp
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

class RadialNeuron:
    def __init__(self, x):
        self.c = x
    
    def count(self, x):
        return exp(-((x - self.c) ** 2) / ((2 * 1.5 ** 2)))

values = [
    [-2.0, -0.48],
    [-1.5, -0.78],
    [-1.0, -0.83],
    [-0.5, -0.67],
    [0.0, -0.20],
    [0.5, 0.70],
    [1.0, 1.48],
    [1.6, 1.17],
    [2.0, 0.20]
]

neurons = [RadialNeuron(values[2 * i][0]) for i in range(5)]
h = np.array([[neurons[i].count(values[j][0]) for i in range(5)] for j in range(9)])

print()
for i in range(len(h)):
    s = ""
    for j in range(len(h[0])):
        s += str(h[i][j]) + " "
    print(s)

y = np.array([[values[j][1]] for j in range(9)])
w = np.dot(LA.inv(np.dot(h.transpose(), h)), np.dot(h.transpose(), y))
h_T_h = np.dot(h.transpose(), h)
h_minusOne = LA.inv(h_T_h)
h_T_y = np.dot(h.transpose(), y)
result = np.dot(h_minusOne, h_T_y)

print()
for i in range(len(w)):
    s = ""
    for j in range(len(w[0])):
        s += str(w[i][j]) + " "
    print(s)

x = [value[0] for value in values]
y1 = [value[1] for value in values]
y2 = [sum([neurons[i].count(value[0]) * w[i][0] for i in range(5)]) for value in values]

print()
for i in range(len(y2)):
    print(y2[i])

n = len(x)
s = 0
for i in range(n):
    s += abs(1 - y1[i] / y2[i])
print(f"Средняя относительная ошибка аппроксимации: {s / n * 100}%")

plt.scatter(x, y1, c="red", label="Исходные точки")
plt.plot(x, y2, label="Полученная аппроксимирующая зависимость")
plt.legend()
plt.grid(True)
plt.show()
