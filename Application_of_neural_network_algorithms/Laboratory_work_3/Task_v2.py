
#Вводные:
#Нейросеть состоит из 5 нейронов, имеет 1 выход
#Обучающие данные: 9 входов и 9 соответствующих выходов
#Используется функция Гаусса, евклидова норма
#Для радиальных элементов есть центры и радиусы

import math as mt
import random as rnd

def matrix_transposition(matrix):
    """
    Функция, которая транспонирует матрицу
    Args: matrix - исходная матрица
    Return: транспонированная матрица
    """
    row_len = len(matrix)
    column_len = len(matrix[0])
    result_matrix = [[0 for i in range(row_len)] for j in range(column_len)]
    for i in range(row_len):
        for j in range(column_len):
            result_matrix[j][i] = matrix[i][j]
    return result_matrix

def matrix_multiplication(matrix_1, matrix_2):
    """
    Функция, которая умножает 2 матрицы
    Args: matrix_1 - первая матрица; matrix_2 - вторая матрица
    Return: результирующая матрица
    """
    result_matrix = [[0 for i in range(len(matrix_2[0]))] for j in range(len(matrix_1))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result_matrix

def determinant_of_matrix(matrix):
    """
    Функция, которая считает определитель квадратной матрицы
    Args: matrix - матрица
    Return: определитель матрицы
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    determinant = 0
    for i in range(n):
        sign = (-1) ** i
        sub_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        determinant += sign * matrix[0][i] * determinant_of_matrix(sub_matrix)
    return determinant

def rising_matrix_to_minusOne(matrix):
    """
    Функция, которая возводит матрицу в степень -1
    Args: matrix - матрица
    Return: матрица, возведённая в степень -1
    """
    determinant = determinant_of_matrix(matrix)
    result_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            #Возведение в степень -1 - это умножение матрицы на 1/определитель
            result_matrix[i][j] += (1 / determinant) * matrix[i][j]
    return result_matrix

class Neuron:
    w = 0

    def __init__(self):
        """
        Функция, которая инициализирует вес нейрону
        Args: отсутствуют
        Return: отсутствует
        """
        self.w = rnd.uniform(-1.0, 1.0)

    def summat(self, x):
        """
        Функция-сумматор нейрона
        Args: x - входное значение
        Return: выходной сигнал нейрона
        """
        #+1 в ответе - порог
        return self.w * x + 1

class Neural_Network:

    def gauss_fun(self, x, centers, radius):
        """
        Функция Гаусса (многомерный случай)
        Args: x - входное значение; centers - список центров радиальных элементов, radius - радиус радиальных элементов
        Return: значение функции
        """
        norm_of_vector = mt.sqrt(sum([mt.pow(x - centers_i, 2) for centers_i in centers]))
        #Сказано, что a = 1/2radius^2
        a = 1 / (2 * mt.pow(radius, 2))
        return mt.exp(-a * norm_of_vector)

    def calculate_characteristic_matrix(self, neurons_quantity, entrances_x, neurons, centers, radius):
        """
        Функция расчёта характеристической матрицы значений радиально-симметричных элементов
        Args: neurons_quantity - количество нейронов; entrances_x - список входных данных, neurons - список нейронов (радиальных элементов); centers - список центров радиальных элементов; radius - радиус радиальных элементов
        Return: характеристическая матрица
        """
        g = [[0 for i in range(neurons_quantity)] for j in range(len(entrances_x))]
        for i in range(len(entrances_x)):
            for j in range(len(neurons)):
                g[i][j] += self.gauss_fun(neurons[j].summat(entrances_x[i][0]), centers, radius)
        return g

    def calculate_matrix_weight_coefficients(self, matrix_h, matrix_y):
        """
        Функция расчёта матрицы весовых коэффициентов
        Args: matrix_h - характеристическая матрица значений радиально-симметричных элементов; matrix_y - матрица выходов обучающих примеров
        Return: вектор-столбец
        """
        return matrix_multiplication((matrix_multiplication((rising_matrix_to_minusOne(matrix_multiplication(matrix_transposition(matrix_h), matrix_h))), matrix_transposition(matrix_h))), matrix_y)

neurons_quantity = 5
entrances_x = [[-2.0], [-1.5], [-1.0], [-0.5], [0.0], [0.5], [1.0], [1.5], [2.0]]
outputs_y = [[-0.48], [-0.78], [-0.83], [-0.67], [-0.2], [0.7], [1.48], [1.17], [0.2]]
#Взяли центры как 1, 3, 5, 7, 9 входной параметр
centers = [-2.0, -1.0, 0.0, 1.0, 2.0]
#Сказано, что r можно просто взять = 1.5
radius = 1.5

neural_network = Neural_Network()
neurons = [Neuron() for i in range(neurons_quantity)]

tmp_res = neural_network.calculate_characteristic_matrix(neurons_quantity, entrances_x, neurons, centers, radius)
res = neural_network.calculate_matrix_weight_coefficients(tmp_res, outputs_y)
for i in range(len(res)):
    s = ""
    for j in range(len(res[0])):
        s += str(res[i][j]) + " "
    print(s)

#Итог - уже почти не помойка, многие функции переписаны и работают правильно, но сам алгоритм нужно переделать
