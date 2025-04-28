#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []

my_family.extend(['Папа', 'Мама', 'Эмилия', 'Есения'])

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]

del my_family_height[0]
my_family_height.extend([[my_family[0], 172], [my_family[1], 167], [my_family[2], 145], [my_family[3], 120]])
print(my_family_height)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print('Рост отца -', my_family_height[0][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

total_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1]

print('Общий рост моей семьи -', total_height, 'см')
