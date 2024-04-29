
#Простенький пример работы метода дихотомии
#Функция: f(x) = x^2-2x+3; betta = 0.2; epsilon = 0.5; отрезок l_0 = [-3; 7]

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import math as mt

def f(x: float) -> float:
    """
    Функция, которая возвращает значение исходной функции в точке х
    Args: x - переменная
    Return: значение функции в точке x
    """
    return x**2 - 2*x + 3

def new_x_0_y_0(l: list[float], betta: float) -> float:
    """
    Функция, которая вычисляет новые переменные x_0 и y_0
    Args: l - отрезок локализации; betta - параметр шага
    Return: новые переменные x_0 и y_0
    """
    x_0 = (l[0] + l[1] - betta) / 2
    y_0 = (l[0] + l[1] + betta) / 2
    return x_0, y_0

def norm_l(l: list[float]) -> float:
    """
    Функция, которая вычисляет норму отрезка локализации
    Args: l - отрезок локализации
    Return: значение нормы отрезка локализации
    """
    return abs(l[1] - l[0])

l_0 = [-3, 7]
betta = 0.2
epsilon = 0.5
k = 0
all_x = []

while True:
    #шаг 3
    x_0, y_0 = new_x_0_y_0(l_0, betta)
    #шаг 4
    f_x_0 = f(x_0)
    f_y_0 = f(y_0)
    #шаг 5
    if f_x_0 < f_y_0:
        l_0[1] = y_0
    else:
        l_0[0] = x_0
    #шаг 6
    norm_l_0 = norm_l(l_0)
    all_x.append((l_0[0] + l_0[1]) / 2)
    if norm_l_0 < epsilon:
        x_min = (l_0[0] + l_0[1]) / 2
        f_min = f(x_min)
        break
    else:
        k += 1

print(f"l = {l_0}, k = {k}, x_min = {x_min}, f_min = {f_min}, all_x = {all_x}")

all_scat = np.array(all_x) #массив всех точек минимума каждой итерации
all_f_y = f(all_scat) #массив значений функции для этих точек
fig, ax = plt.subplots() #создание фигуры и оси х
x_range = np.linspace(-0.75, 1.75, 400)
y_range = f(x_range)
scat = ax.scatter([], [], color="blue", label="Точки минимума на каждой итерации") #задаём объект, который будет отображать точки
ax.set(xlim=[-1, 2], ylim=[1.0, 7.0], xlabel="x", ylabel="f(x)")
ax.legend()

def update(frame: int) -> object:
    """
    Функция, которая перерисовывает общий график (моментально рисует график функции, с интервалом добавляет точки с номером и стрелкой между парой точек, а для последней - значение)
    Args: frame - кадр, в который как-то изменяется график
    Return: ссылка на объект-точку (наверное)
    """
    if frame == 0:
        plt.plot(x_range, f(x_range), label="f(x)", color="blue") #моментально рисуем основную функцию
    scat.set_offsets(np.c_[all_scat[:mt.ceil(frame / 10)], all_f_y[:mt.ceil(frame / 10)]]) #каждые 10 кадров рисуем точки
    for i, txt in enumerate(all_f_y[:mt.ceil(frame / 10)]):
        ax.annotate(f"{i+1}", (all_scat[i], txt), textcoords="offset points", xytext=(0,10), ha="center") #добавляем подпись точкам (их порядковый номер)
        if i > 0:
            #поясняю за аргументы: arrowprops - задание стрелки; arrowstyle - вид стрелки; connectionstyle - вид соединения (в нашем случае арка с радиусом)
            ax.annotate("", xy=(all_scat[i], all_f_y[i]), xytext=(all_scat[i-1], all_f_y[i-1]), arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=1")) #добавляем стрелки от точки к точке
        if i == 5:
            #поясняю за аргументы: textcoords - система координат для положения текста (offset points - смещение относительно точки); xytext - смещение текста относительно точки; ha - выравнивание текста по горизонтали; va - выравнивание по вертикали
            ax.annotate(f"{txt:.2f}", (all_scat[i], txt), textcoords="offset points", xytext=(0,-10), ha="center", va="top") #добавляем последней точке значение функции
    return (scat)

animation = anim.FuncAnimation(fig=fig, func=update, frames=60, interval=30, repeat=False) #вызываем анимацию, которая будет вызывать покадрово функцию update
#animation.save("dihotomia.gif", writer="imagemagick") #сохранение сразу в .gif, но страдает плавность
#animation.save("frame.png", writer="imagemagick") #сохранение покадрово в .png для конвертации в .gif
plt.show()
