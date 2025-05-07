# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
from simple_draw import COLOR_PURPLE

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

for y in range(0, 700, 50):
    for x in range(-50, 700, 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x + 100, y)
        sd.line(start_point=start_point, end_point=end_point, color=COLOR_PURPLE, width=2)

for x in range(-50, 700, 100):
    for y in range(0, 700, 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x, y + 50)
        sd.line(start_point=start_point, end_point=end_point, color=COLOR_PURPLE, width=2)

for x in range(0, 700, 100):
    for y in range(50, 700, 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x, y + 50)
        sd.line(start_point=start_point, end_point=end_point, color=COLOR_PURPLE, width=2)

sd.pause()
