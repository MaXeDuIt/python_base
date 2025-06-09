# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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
    for _ in range(3):
        next_point = draw_vector(point=next_point, angle=angle, length=length)
        angle += 90
    sd.line(start_point=next_point, end_point=point, width=2)

def pentagon(point, angle, length):
    next_point = point
    for _ in range(4):
        next_point = draw_vector(point=next_point, angle=angle, length=length)
        angle += 72
    sd.line(start_point=next_point, end_point=point, width=2)

def hexagon(point, angle, length):
    next_point = point
    for _ in range(5):
        next_point = draw_vector(point=next_point, angle=angle, length=length)
        angle += 60
    sd.line(start_point=next_point, end_point=point, width=2)


figure_list = ['Треугольник', 'Квадрат', 'Пятиугольник', 'Шестиугольник']


print('Возможные фигуры:')
for i, col in enumerate(figure_list):
    print(i, ':', col)

while True:
    number_color = input('Введите желаемую фигуру => ')
    result = int(number_color)
    point = sd.get_point(250, 300)
    if result == 0:
        triangle(point, 0, 100)
        break
    elif result == 1:
        square(point, 0, 100)
        break
    elif result == 2:
        pentagon(point, 0, 100)
        break
    elif result == 3:
        hexagon(point, 0, 100)
        break
    else:
        print('Вы ввели некорректный номер фигуры!')

sd.pause()
