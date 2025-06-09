# -*- coding: utf-8 -*-
import simple_draw as sd
from simple_draw import COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

color_list = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
color_dict = {0: COLOR_RED, 1: COLOR_ORANGE, 2: COLOR_YELLOW, 3: COLOR_GREEN,
              4: COLOR_CYAN, 5: COLOR_BLUE, 6: COLOR_PURPLE}

def draw_vector(point, angle, length, color):
    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw(color=color)
    return vector.end_point

def triangle(point, angle, length, color):
    next_point = point
    for _ in range(2):
        next_point = draw_vector(point=next_point, angle=angle, length=length, color=color)
        angle += 120
    sd.line(start_point=next_point, end_point=point, width=2, color=color)

def square(point, angle, length, color):
    next_point = point
    for i in range(3):
        next_point = draw_vector(point=next_point, angle=angle, length=length, color=color)
        angle += 90
    sd.line(start_point=next_point, end_point=point, width=2, color=color)

def pentagon(point, angle, length, color):
    next_point = point
    for i in range(4):
        next_point = draw_vector(point=next_point, angle=angle, length=length, color=color)
        angle += 72
    sd.line(start_point=next_point, end_point=point, width=2, color=color)

def hexagon(point, angle, length, color):
    next_point = point
    for i in range(5):
        next_point = draw_vector(point=next_point, angle=angle, length=length, color=color)
        angle += 60
    sd.line(start_point=next_point, end_point=point, width=2, color=color)


print('Возможные цвета:')
for i, col in enumerate(color_list):
    print(i, ':', col)

while True:
    number_color = input('Введите желаемый цвет => ')
    result = int(number_color)
    if 0 <= result <= 6:
        print('OK')
        point_1 = sd.get_point(100, 400)
        triangle(point_1, 10, 100, color=color_dict[result])

        point_2 = sd.get_point(400, 400)
        square(point_2, 20, 100, color=color_dict[result])

        point_3 = sd.get_point(150, 100)
        pentagon(point_3, 30, 100, color=color_dict[result])

        point_4 = sd.get_point(450, 100)
        hexagon(point_4, 40, 100, color=color_dict[result])
        break
    else:
        print('Вы ввели некорректный номер цвета!')

sd.pause()
