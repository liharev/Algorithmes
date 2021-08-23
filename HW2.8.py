num = list(input("Введите любое целое число: "))
digit = int(input("Какую цифру ищем? "))
print(f'{digit} встречается {num.count(str(digit))} раз')