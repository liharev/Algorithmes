while True:
    try:
        digits = list(str(int(input("Введите натуральное число: "))))
        break
    except TypeError:
        print('Ошибка ввода. Попробуйте снова.')
even = 0
odd = 0
for digit in digits:
    if int(digit) % 2 == 0:
        even += 1
    else:
        odd +=1
print(f'В данном числе {even} четных и {odd} нечетных цифр')
