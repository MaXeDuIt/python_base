# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: координата X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    point_head = sd.get_point(x, y)
    sd.circle(center_position=point_head, radius=45, color=color)
    point_left_eye = sd.get_point(x - 17, y + 17)
    sd.circle(center_position=point_left_eye, radius=5, color=color)
    point_right_eye = sd.get_point(x + 17, y + 17)
    sd.circle(center_position=point_right_eye, radius=5, color=color)
    point_nose_start = sd.get_point(x, y + 5)
    point_nose_end = sd.get_point(x, y - 10)
    sd.line(start_point=point_nose_start, end_point=point_nose_end, color=color)
    point_mouth_left = sd.get_point(x - 25, y - 10)
    point_mouth_center_start = sd.get_point(x - 10, y - 20)
    sd.line(start_point=point_mouth_left, end_point=point_mouth_center_start, color=color)
    point_mouth_center_end = sd.get_point(x + 10, y - 20)
    sd.line(start_point=point_mouth_center_start, end_point=point_mouth_center_end, color=color)
    point_mouth_right = sd.get_point(x + 25, y - 10)
    sd.line(start_point=point_mouth_center_end, end_point=point_mouth_right, color=color)


smiles_color = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

for _ in range(10):
    coord_x = random.randint(50, 550)
    coord_y = random.randint(50, 550)
    color_smile = random.choice(smiles_color)
    smile(x=coord_x, y=coord_y, color=color_smile)

sd.pause()