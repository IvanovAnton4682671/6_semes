
#Входные данные: 7 входных параметров (по-факту, есть 8-ой входной сигнал, но он - правильный ответ); ->
# -> 4 нейрона; выход - 4 разных кластера; имеется 20 обучающих примеров -> 20 корректировок весов
#Требования - learning_rate = 0.3, и уменьшается на 0.3 каждую эпоху (всего 6 эпох); реализовать сеть Кохонена

import random as rnd
import math as mt

def normalizing_fun(list_of_list_of_int):
    """
    Функция, которая нормализует входные данные
    Args: list_of_list_of_int - список списков int-значений (о как)
    Return: нормализованный массив
    """
    result = [[0 for _ in range(len(list_of_list_of_int[0]))] for _ in range(len(list_of_list_of_int))]
    for i in range(len(list_of_list_of_int)):
        for j in range(len(list_of_list_of_int[0])):
            mean = sum(list_of_list_of_int[i]) / len(list_of_list_of_int[0])
            #пробовал не / mean, a - mean (тогда у всех нейронов одинаковый результат)
            result[i][j] = list_of_list_of_int[i][j] / (mean * 5)
    return result

class Neuron:

    #веса нейрона
    weights = []

    def __init__(self, num_of_inputs):
        """
        Функция, которая инициализирует веса нейрону
        Args: num_of_inputs - кол-во входных сигналов
        Return: отсутствует
        """
        self.weights = [rnd.uniform(-1.0, 1.0) for _ in range(num_of_inputs)]

    def summat(self, list_of_inputs):
        """
        Функция-сумматор нейрона
        Args: list_of_inputs - список входных данных
        Return: выход нейрона
        """
        #прибавляем 1 - это порог
        return 1 + sum(self.weights[i] * list_of_inputs[i] for i in range(len(list_of_inputs)))

    def activation_func(self, input_x):
        """
        Функция активации нейрона (гиперболический тангенс)
        Args: input_x - входной параметр
        Return: значение функции
        """
        #тут появилась ошибка math range error
        #return (mt.exp(2 * input_x) - 1) / (mt.exp(2 * input_x) + 1)
        return mt.tanh(input_x)
        #теперь попробуем сигмоиду (хрень, результат тот же, да и иногда вылетает math range error)
        #return 1 / (1 + mt.exp(-input_x))

    def gradient_descent(self, gradient, learning_rate):
        """
        Функция, которая обучает нейроны (корректирует веса) методом градиентного спуска
        Args: gradient - градиент обратного распространения ошибки; learning_rate - скорость обучения
        Return: отсутствует
        """
        for i in range(len(self.weights)):
            self.weights[i] -= gradient[i] * learning_rate

class Neural_Network:

    def __init__(self):
        """
        Функция, которая создаёт нейросети пустой массив для хранения выходов нейронов по примерам
        Args: отсутствуют
        Return: отсутствует
        """
        self.neurons_outputs = []

    #выяснилось, что эта ошибка хорошо подходит для нейросетей регрессии, но не для нейросетей классификации
    def mse_less(self, list_of_answers, neurons_outputs):
        """
        Функция, которая считает среднеквадратичную ошибку
        Args: list_of_answers - список желаемых ответов; neurons_outputs - выходы нейронов
        Return: среднеквадратичная ошибка
        """
        error = sum(mt.pow(list_of_answers[i] - neurons_outputs[i], 2) for i in range(len(list_of_answers)))
        return error / len(list_of_answers)

    #вот это уже другой разговор, но, к сожалению, под эту функцию нужно переписывать не только алгоритм ->
    # -> обучения, но и расчёт градиента и обновление весов(((
    def cross_entropy_loss_fun(self, list_of_inputs, list_of_answers, neurons_outs):
        """
        Кросс-энтропийная функция потерь (как звучит-то, а!)
        Args: list_of_inputs - ; list_of_answers - ; neurons_outs - 
        Return: ошибка сети
        """
        result = 0
        n = len(list_of_inputs)
        tmp = 0
        for i in range(len(n)):
            #тут ещё и логарифм, вообще крутая функция
            #здесь sum(neurons[i]) / 4 - средний выход сети для конкретного примера, потому что в формуле ->
            # -> используется просто выход сети (хз, как они его там считают)
            tmp += (list_of_answers[i][0] * mt.log(sum(neurons_outs[i]) / 4, base=mt.e)) + ((1 - list_of_answers[i][0]) * mt.log(1 - sum(neurons_outs[i]) / 4, base=mt.e))
        result = (-1 / n) * tmp
        return result

    #использую среднюю ошибку, потому что, а как иначе?
    #цикл идёт по примерам, а потом уже по нейронам (входных 7, а нейронов 4 - list index out)
    #уже всё хорошо, не используем среднюю ошибку
    def calculate_gradient(self, list_of_inputs, list_of_answers, average_error):
        """
        Функция, которая рассчитывает градиент методом обратного распространения ошибки
        Args: list_of_inputs - список входных параметров; list_of_answers - список желаемых выходов; average_error - средняя ошибка
        Return: градиент
        """
        gradient = []
        for i in range(len(list_of_inputs[0])):
            #gradient.append((1 / len(list_of_answers)) * list_of_inputs[i] * average_error)
            #теперь рассчитываем градиент для каждого веса, а не одинаковый для всех, как раньше
            gradient.append((1 / len(list_of_answers)) * sum(list_of_inputs[j][i] * (list_of_answers[j] - self.neurons_outputs[j]) for j in range(len(list_of_answers))))
        return gradient

    def learning_algorithm(self, learning_rate, list_of_inputs, list_of_outputs, neurons):
        """
        Функция, которая реализует алгоритм обучения нейросети
        Args: learning_rate - скорость обучения; list_of_inputs - список входных параметров; list_of_outputs - список желаемых выходов; neurons - список нейронов
        Return: отсутствует
        """
        while learning_rate > 0.0:
            for i in range(len(list_of_inputs)):
                #список ошибок всех нейронов для одного примера
                errors = []
                #список выходов нейронов для одного примера
                neurons_outs = []
                for j in range(len(neurons)):
                    #выход нейрона
                    neuron_out = neurons[j].activation_func(neurons[j].summat(list_of_inputs[i]))
                    neurons_outs.append(neuron_out)
                    #ошибка нейрона
                    error = self.mse_less([list_of_outputs[i][0]], [neuron_out])
                    errors.append(error)
                #заполняем массив для хранения по примерам
                self.neurons_outputs = neurons_outs
                #средняя ошибка
                average_error = sum(errors) / len(errors)
                #градиент
                gradient = self.calculate_gradient(list_of_inputs, list_of_outputs[i], average_error)
                for j in range(len(neurons)):
                    neurons[j].gradient_descent(gradient, learning_rate)
                print(neurons[0].weights)
                print(errors)
            learning_rate -= 0.00005

    def testing(self, neurons, list_of_inputs, list_of_outputs):
        """
        Функция, которая показывает результат работы нейросети
        Args: neurons - список нейронов; list_of_inputs - список входных данных; list_of_outputs - список желаемых выходов
        """
        for i in range(len(list_of_inputs)):
            #список выходов нейронов
            neurons_outs = []
            for j in range(len(neurons)):
                neuron_out = neurons[j].activation_func(neurons[j].summat(list_of_inputs[i]))
                neurons_outs.append(neuron_out)
            #среднее значение выхода
            mean = sum(neurons_outs) / len(neurons_outs)
            #блок колдунства
            if 1.0 < mean < 1.1: mean = 1.75
            elif 0.9 < mean < 1.0: mean = 1.50
            elif 0.8 < mean < 0.9: mean = 1.25
            elif 0.7 < mean < 0.8: mean = 1
            else: mean = 0
            print(f"Выход нейронов: {neurons_outs}; средний выход: {mean}; желаемый выход: {list_of_outputs[i][0]}")

#кол-во нейронов
neurons_quantity = 4
#входные параметры
inputs_x = [
    [1, 1, 60, 79, 60, 72, 63],
    [1, 0, 60, 61, 30, 5, 17],
    [0, 0, 60, 61, 30, 66, 58],
    [1, 1, 85, 78, 72, 70, 85],
    [0, 1, 65, 78, 60, 67, 65],
    [0, 1, 60, 78, 77, 81, 60],
    [0, 1, 55, 79, 56, 69, 72],
    [1, 0, 55, 56, 50, 56, 60],
    [1, 0, 55, 60, 21, 64, 50],
    [1, 0, 60, 56, 30, 16, 17],
    [0, 1, 85, 89, 85, 92, 85],
    [0, 1, 60, 88, 76, 66, 60],
    [1, 0, 55, 64, 0, 9, 50],
    [0, 1, 80, 83, 62, 72, 72],
    [1, 0, 55, 10, 3, 8, 50],
    [0, 1, 60, 67, 57, 64, 50],
    [1, 1, 75, 98, 86, 82, 85],
    [0, 1, 85, 85, 81, 85, 72],
    [1, 1, 80, 56, 50, 69, 50],
    [1, 0, 55, 60, 30, 8, 60]
]
print(f"Нормализованные входные параметры: {normalizing_fun(inputs_x)}")
#желаемые выходы (да да, кластеров 4, а возможных выходов - 5 (очередной прикол))
outputs_y = [
    [1], [0], [0], [1.25], [1],
    [1.25], [0], [0], [0], [0],
    [1.75], [1.25], [0], [1.25], [0],
    [0], [1.50], [1.25], [0], [0]
]
#скорость обучения (при настройке 0.30 веса "взрываются")
learning_rate = 0.001
#список нейронов
neurons = [Neuron(len(inputs_x[0])) for _ in range(neurons_quantity)]
#нейросеть
neural_network = Neural_Network()
#проверяем нейросеть до обучения
print()
print("Нейросеть до обучения")
neural_network.testing(neurons, normalizing_fun(inputs_x), outputs_y)
#запускаем алгоритм обучения сети
neural_network.learning_algorithm(learning_rate, normalizing_fun(inputs_x), outputs_y, neurons)
#проверяем нейросеть после обучения
print()
print("Нейросеть после обучения")
neural_network.testing(neurons, normalizing_fun(inputs_x), outputs_y)

#Итог - снова попахивает мусором, работает некорректно
