while True:
    try:
        digits = list(str(int(input("Введите натуральное число: "))))
        break
    except TypeError:
        print('Ошибка ввода. Попробуйте снова.')
print(''.join(list(reversed(digits))))