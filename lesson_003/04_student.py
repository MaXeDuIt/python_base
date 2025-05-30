# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
parents = 0
month = 1
percent_expenses = 0.03

while month <= 10:
    if month == 1:
        parents = expenses - educational_grant
        month += 1
        continue
    expenses += expenses * percent_expenses
    parents += expenses - educational_grant
    month += 1

print('Студенту надо попросить', round(parents, 2), 'рублей')
