import random
while True:
    try:
        start, finish = map(ord, input("Введите диапазон значений: ").split())
        break
    except TypeError:
        print('Ошибка ввода. Попробуйте снова.')
print(chr(random.randrange(start, finish, 1)))

