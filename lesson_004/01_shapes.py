# -*- coding: utf-8 -*-

import simple_draw as sd
from Tools.scripts.var_access_benchmark import write_dict


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def triangle(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=2)
#     v3.draw()
#
# def square(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=2)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=2)
#     v4.draw()
#
# def pentagon(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=2)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=2)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=2)
#     v5.draw()
#
# def hexagon(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=2)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=2)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=2)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=2)
#     v5.draw()
#
#     v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=2)
#     v6.draw()
#
#
# point_1 = sd.get_point(75, 400)
# triangle(point_1, 0, 150)
#
# point_2 = sd.get_point(400, 400)
# square(point_2, 0, 150)
#
# point_3 = sd.get_point(100, 100)
# pentagon(point_3, 0, 100)
#
# point_4 = sd.get_point(425, 100)
# hexagon(point_4, 0, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

def draw_vector(point, angle, length):
    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw()
    return vector.end_point

def triangle(point, angle, length):
    next_point = point
    for _ in range(2):
        next_point = draw_vector(point=next_point, angle=angle, length=length)
        angle += 120
    sd.line(start_point=next_point, end_point=point, width=2)

def square(point, angle, length):
    next_point = point
    for i in range(3):
        next_point = draw_vector(point=next_point, angle=angle, length=length)
        angle += 90
    sd.line(start_point=next_point, end_point=point, width=2)

def pentagon(point, angle, length):
    next_point = point
    for i in range(4):
        next_point = draw_vector(point=next_point, angle=angle, length=length)
        angle += 72
    sd.line(start_point=next_point, end_point=point, width=2)

def hexagon(point, angle, length):
    next_point = point
    for i in range(5):
        next_point = draw_vector(point=next_point, angle=angle, length=length)
        angle += 60
    sd.line(start_point=next_point, end_point=point, width=2)



point_1 = sd.get_point(100, 400)
triangle(point_1, 10, 100)

point_2 = sd.get_point(400, 400)
square(point_2, 20, 100)

point_3 = sd.get_point(150, 100)
pentagon(point_3, 30, 100)

point_4 = sd.get_point(450, 100)
hexagon(point_4, 40, 100)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
