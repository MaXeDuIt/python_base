# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

sd.resolution = (1200, 600)

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

total_list = []

for _ in range(N):
    x = sd.random_number(100, 900)
    y = sd.random_number(600, 900)
    length = sd.random_number(10, 100)
    list_snowflakes = [x, y, length]
    total_list.append(list_snowflakes)

while True:
    sd.start_drawing()
    for snowflake in total_list:
        # x = snowflake[0]
        # y = snowflake[1]
        point = sd.get_point(snowflake[0], snowflake[1])
        length = snowflake[2]
        sd.snowflake(center=point, length=length, color=sd.background_color)
        snowflake[0] += 5
        snowflake[1] -= 15
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, length=length, color=sd.COLOR_WHITE)
    if total_list[0][1] < 10:
        break
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

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


sd.pause()