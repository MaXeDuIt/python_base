# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# x0, y0 = 50, 50
# x1, y1 = 350, 450
# step = 5
#
# for color in rainbow_colors:
#     start_point = sd.get_point(x0, y0)
#     end_point = sd.get_point(x1, y1)
#     sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
#     x0 += step
#     x1 += step


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

x, y = 400, 0
radius = 450
step = 20

for color in rainbow_colors:
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=radius, color=color, width=step)
    radius += step

sd.pause()
