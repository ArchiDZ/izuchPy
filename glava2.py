import math
def ex_2_1():
    print('Вариант А')
    print('Формула y=17x^2-6x+13')
    num_x = 22
    result_a = 17*(num_x*num_x)-6*num_x+13
    print(f'Результат вычеслений: {result_a}')

def ex_2_2(num_a):
    chislitel = (num_a**2)+10
    znamenatel = math.sqrt(num_a**2)+1
    result = chislitel / znamenatel
    print(f'результат вычислений: {round(result,2)}')

def ex_2_3(num_a, num_x):
    print('Вариант А')
