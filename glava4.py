import math
def ex_4_1():
    num_x = 9
    num_y = 7
    print (f'Сравнение чисел {num_x} и {num_y}')
    if num_x > num_y:
        print('первое число больше, а второе меньше')
    else:
        print('Первое число меньше, а второе больше')

def ex_4_2(num_x):
    if num_x > 0:
        y = math.sin(num_x**2)
        print(y)
    else:
        y = 1-2*math.sin(num_x**2)
        print(y)
