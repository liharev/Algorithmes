while True:
    try:
        year = int(input("Введите год: "))
        break
    except ValueError or TypeError:
        print('Вы ввели не делое число. Попробуйте снова.')
leapyear = year % 4
if leapyear == 0:
    print("Этот год високосный")
else:
    print("Этот год невисокосный")

