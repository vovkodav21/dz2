# Бонусні завдання:

# 6. * Програма отримує на вхід число х.

# Даний список із 10 елементів [10, 20, 30, 40, 50, 60, 70, 80, 90, 100].

# Написати програму яка поверне:

# Чи є x серед елементів.


# Число на введення може бути як цілим числом, числом з точкою, що плаває, так і від'ємним,

# тобто. x = -10.00 має повернути що x є у списку.

# ** В ідеалі список повинен бути записаний як кортеж один раз.


input_X = float(input("Введіть будь-яке число: "))
whiskey_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
kilo_list = list(map(float, whiskey_list))
limalist = list(map(lambda x: -x, kilo_list))
alpha_list = kilo_list + limalist

if input_X in alpha_list:
    print('число є в списку')
else:
    print('Число не є в списку')
