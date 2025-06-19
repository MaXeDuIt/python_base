# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 100

sd.resolution = (1200, 600)

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# total_list = []
#
# for _ in range(N):
#     x = sd.random_number(100, 900)
#     y = sd.random_number(600, 900)
#     length = sd.random_number(10, 100)
#     list_snowflakes = [x, y, length]
#     total_list.append(list_snowflakes)
#
# while True:
#     sd.start_drawing()
#     for snowflake in total_list:
#         point = sd.get_point(snowflake[0], snowflake[1])
#         length = snowflake[2]
#         sd.snowflake(center=point, length=length, color=sd.background_color)
#         snowflake[0] += 5
#         snowflake[1] -= 15
#         point = sd.get_point(snowflake[0], snowflake[1])
#         sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
#     if total_list[0][1] < 10:
#         break
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

total_list = []

for _ in range(N):
    x = sd.random_number(100, 1100)
    y = 700
    length = sd.random_number(5, 15)
    factor_a = sd.random_number(1, 8)/10
    factor_b = sd.random_number(1, 7)/10
    factor_c = sd.random_number(35, 65)
    list_snowflakes = [x, y, length, factor_a, factor_b, factor_c]
    total_list.append(list_snowflakes)

while True:
    sd.start_drawing()
    for snowflake in total_list:
        point = sd.get_point(snowflake[0], snowflake[1])
        length = snowflake[2]
        factor_a = snowflake[3]
        factor_b = snowflake[4]
        factor_c = snowflake[5]
        sd.snowflake(center=point, length=length, color=sd.background_color,
                     factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        wind_x = sd.random_number(-15, 15)
        wind_y = sd.random_number(5, 15)
        snowflake[0] += wind_x
        snowflake[1] -= wind_y
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE,
                     factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        if snowflake[1] < 10:
            sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE,
                         factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
            snowflake[1] = 700
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()