import operator
def mydiv(x,y):
    if y==0:
        return "Ошибка. Деление на ноль."
    else:
        return x/y
def operation(sign,x,y):
    return {
        sign == "+": x+y,
        sign == "-": x-y,
        sign == "*": x*y,
        sign == "/": mydiv(x,y)
    }
while True:
    abc = list(map(str, input("Введите числа и оператор через пробел: ").split(maxsplit=3)))
    try:
        a = float(abc[0])
        sign = abc[1]
        b = float(abc[2])
    except (IndexError, ValueError, TypeError):
        print('Ошибка ввода. Попробуйте снова.')
        continue
    if sign=="0":
        print('конец программы')
        break
    print("Результат = " + str(operation(sign, a, b).get(True)))





