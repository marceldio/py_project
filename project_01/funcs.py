def sum_(a, b):
    sum_ = a + b
    print(f'Сумма: {sum_}')

def dif_(a, b):
    dif_ = a - b
    print(f'Разность: {dif_}')


a, b = map(int, input('Введите два числа через пробел: ').split())

sum_(a, b)
dif_(a, b)
