# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# 1)
# def draw_branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v1.draw()
#     return v1.end_point
#
# root_point = sd.get_point(300, 30)
# angle_0 = 90
# length_0 = 100
#
# next_point_1 = root_point
# next_point_2 = root_point
# next_angle_right = angle_0
# next_angle_left = angle_0
# next_length = length_0
#
# for i in range(5):
#     next_point_1 = draw_branches(point=next_point_1, angle=next_angle_right, length=next_length)
#     next_point_2 = draw_branches(point=next_point_2, angle=next_angle_left, length=next_length)
#     next_angle_right -= 30
#     next_angle_left += 30
#     next_length -= 20


# 2)
# def draw_branches(point, angle, length, delta):
#     if length < 2:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle_right = angle - delta
#     next_angle_left = angle + delta
#     next_length = length * .75
#     draw_branches(point=next_point, angle=next_angle_right, length=next_length, delta = delta)
#     draw_branches(point=next_point, angle=next_angle_left, length=next_length, delta=delta)
#
#
# root_point = sd.get_point(300, 30)
# angle_0 = 90
# length_0 = 100
# delta_0 = 30
#
# draw_branches(point=root_point, angle=angle_0, length=length_0, delta=delta_0)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.resolution = (1200, 1000)

def draw_branches(point, angle, length):
    if length < 5:
        return

    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()

    next_point = v1.end_point

    delta = sd.random_number(18, 42)
    next_angle_right = angle - delta
    next_angle_left = angle + delta

    gamma = sd.random_number(60, 90) / 100
    next_length = length * gamma

    draw_branches(point=next_point, angle=next_angle_right, length=next_length)
    draw_branches(point=next_point, angle=next_angle_left, length=next_length)


root_point = sd.get_point(600, 30)
angle_0 = 90
length_0 = 200

draw_branches(point=root_point, angle=angle_0, length=length_0)

sd.pause()