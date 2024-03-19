
#Вводные:
#Есть данная выборка section, где в списке первая переменная - входное Х, а вторая - выходное Y
#Требуется создать аппроксимирующую модель в виде нейронной сети на основе радиально-симметричных функций
#Вход сети - входное значение Х, выход - соответствующее Y
#Сеть состоит из 5 нейронов
#Нужно указать центры и радиусы нейронов (в качестве центров использовать 1, 3, 5, 7 и 9 значения Х) ???
#Использовать функцию Гаусса, евклидову норму, рассчитывать веса по формуле: w = (G^t * G)^(-1) * G^t * y ???

#Некоторые выводы:
#Так как вход это 1 параметр, то у нейронов по 1 весу
#Особенность нейросети на основе радиально-симметричных функций - симметричный отклик относительно ->
# какой-либо вертикальной оси, т.е. можно построить график, у которого будет симметричный шаг
#Аппроксимирующая модель - модель, которая позволяет заменить сложные объекты на более простые ->
# аналоги с сохранением главных черт, т.е. упрощает исходную модель, не изменяя принципов её работы
#Функция Гаусса: g(x) = a * e^(-(x - b)^2 / (2 * c^2)), где a, b, c - произвольные вещественные числа
#Евклидова норма: ||A|| = sqrt(E((a_ij)^2))
#Центры нейронов - есть
#Радиусы нейронов найдём через метод равных интервалов

import math as mt

def euclid_norm(a):
    """
    Евклидова норма матрицы
    Args: a - матрица
    Return: норма матрицы
    """
    res = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            res += mt.pow((a[i][j][0] + a[i][j][1]) / 2, 2)
    return mt.sqrt(res)

def trans_mat(a):
    """
    Функция транспонирования матрицы
    Args: a - матрица
    Return: транспонированная матрица
    """
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]

def multiply_mat(a, b):
    """
    Функция перемножения квадратных матриц с элементами-списками
    Args: a - первая матрица, b - вторая матрица
    Returns: произведение матриц a и b
    """
    n = len(a)
    result_mat = [[[0, 0] for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_mat[i][j][0] += a[i][k][0] * b[k][j][0]
                result_mat[i][j][1] += a[i][k][1] * b[k][j][1]
    return result_mat

def mat_in_extent(a, s):
    """
    Функция возведения матрицу в степень
    Args: a - матрица, s - степень
    Return: матрица в степени
    """
    n = len(a)
    result_mat = [[[0, 0] for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(2):
                result_mat[i][j][k] += mt.pow(a[i][j][k], s)
    return result_mat

def number_in_mat(x):
    """
    Функция преобразования числа в матрицу
    Args: x - число
    Return: матрица из чисел x
    """
    result_mat = [[[x, x] for i in range(3)] for j in range(3)]
    return result_mat

def subtracts_mat(a, b):
    """
    Функция, которая отнимает одну матрицу от другой с элементами списками
    Args: a - первая матрица, b - вторая матрица
    Return: разность матриц a и b
    """
    n = len(a)
    result_mat = [[[0, 0] for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_mat[i][j][0] += a[i][k][0] - b[k][j][0]
                result_mat[i][j][1] += a[i][k][1] - b[k][j][1]
    return result_mat

class Neuron:
    w = 0

#Вот это вот всё тоже надо переделать, скорее всего

    def init_weight(self, g, y_true):
        """
        Инициализация веса нейрона
        Args: g - матрица точек, y_true - выходное значение
        Return: отсутствует
        """
        self.w = multiply_mat(multiply_mat(mat_in_extent(multiply_mat(trans_mat(g), g), -1), trans_mat(g)), number_in_mat(y_true))

    def summat(self, x_in):
        """
        Функция-сумматор нейрона
        Args: x_in - входящий сигнал
        Result: вес * сигнал
        """
        result = euclid_norm(self.w) * x_in
        return result

    def update_weights(self, learning_rate, gradient, y_true):
        """
        Обновление весов нейрона
        Args: learning_rate - коэффициент обучения, gradient - градиент ошибки, y_true - массив правильных ответов
        Return: отсутствует
        """
        tmp = euclid_norm(self.w)
        tmp_2 = 0
        for i in range(len(gradient)):
            tmp_2 += gradient[i] * y_true[i]
        tmp_3 = tmp + learning_rate * tmp_2
        self.w = subtracts_mat(self.w, number_in_mat(tmp_3))

class Neural_Network:
#    def gauss_fun(self, x, a, b, c):
#        """
#        Функция Гаусса
#        Args: x - входное значение, a - амплитуда, b - центр, c - ширина (радиус)
#        Return: значение функции
#        """
#        return a * mt.pow(mt.e, -(mt.pow(x - b, 2) / (2 * mt.pow(c, 2))))
#Если изменить только функцию Гаусса, то ничего не поменяется (быстро увеличиваются веса)
    def gauss_fun(self, x, a, c):
        """
        Функция Гаусса для многомерного случая
        Args: x - входное значение, a - какой-то параметр, который связан с радиусами (берём за 1), c - вектор центров
        Return: значение функции
        """
        tmp = 0
        for i in range(len(c)):
            tmp += mt.pow(x - c[i], 2)
        tmp = mt.sqrt(tmp)
        return mt.exp(-a * tmp)

#Эти 2 функции не нужны, в задаче не идёт речь об обучении методом градиентного спуска и среднеквадратичной ошибки

    def mse_less(self, y_true, y_pred):
        """
        Среднеквадратичная ошибка
        Args: y_true - истинные значения, y_pred - предсказанные значения
        Return: значение ошибки
        """
        return sum([mt.pow(y_true[i] - y_pred[i], 2) for i in range(len(y_true))]) / len(y_true)

    def mse_gradient(self, y_true, y_pred):
        """
        Градиент среднеквадратичной ошибки
        Args: y_true - истинные значения, y_pred - предсказанные значения
        Return: градиент ошибки
        """
        return (1 / 9) * mt.pow(y_true - y_pred, 2)

neurons_quantity = 5
entrances_x = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]
outputs_y = [-0.48, -0.78, -0.83, -0.67, -0.2, 0.7, 1.48, 1.17, 0.2]
centers = [-2.0, -1.0, 0.0, 1.0, 2.0]
#centers = [((i + 1) + i) / 2 for i in range(5)] - альтернатива нахождения центров
radiuses = [sum([mt.sqrt(mt.pow(x - c, 2)) for x in entrances_x]) / len(entrances_x) for c in centers]
g = [[[-2.0, -0.48], [-1.5, -0.78], [-1.0, -0.83]],
     [[-0.5, -0.67], [0.0, -0.2], [0.5, 0.7]],
     [[1.0, 1.48], [1.5, 1.17], [2.0, 0.2]]]
learning_rate = 0.3
epochs = 1000

neural_network = Neural_Network()
neurons = [Neuron() for i in range(neurons_quantity)]
list_characteristics_neurons = [[centers[i], radiuses[i]] for i in range(len(centers))]
for i in range(len(neurons)):
    neurons[i].init_weight(g, outputs_y[i])
for i in range(epochs):
    list_neurons_outputs = []
    list_neurons_errors = []
    list_neurons_gradient = []
    for j in range(len(entrances_x)):
        tmp_neuron_output = 0
        tmp_neuron_error = 0
        tmp_neuron_gradient = 0
        for k in range(len(neurons)):
            result_neuron = neurons[k].summat(entrances_x[j])
            #tmp_neuron_output += neural_network.gauss_fun(result_neuron, 1, list_characteristics_neurons[k][0], list_characteristics_neurons[k][1])
            tmp_neuron_output += neural_network.gauss_fun(result_neuron, 1, centers)
            tmp_neuron_error += neural_network.mse_less([outputs_y[j]], [result_neuron])
            tmp_neuron_gradient += neural_network.mse_gradient(outputs_y[j], result_neuron)
        list_neurons_outputs.append(tmp_neuron_output)
        list_neurons_errors.append(tmp_neuron_error)
        list_neurons_gradient.append(tmp_neuron_gradient)
    if (i + 1) % 50 == 0:
        print(f"Выход нейронов - {tmp_neuron_output}, ошибка - {tmp_neuron_error}, градиент ошибки - {tmp_neuron_gradient}")
    for j in range(len(neurons)):
        neurons[j].update_weights(learning_rate, list_neurons_gradient, outputs_y)
    print(neurons[0].w[0][0])

#Итог - помойка, работает не правильно, надо переделывать
