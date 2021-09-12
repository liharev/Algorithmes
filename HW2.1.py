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
    abc = list(map(str, input("Введите числа и оператор через пробел: ").split(maxsplit=3))) #40+8*3=64bit
    try:
        a = float(abc[0])                                                                    #24bit
        sign = abc[1]                                                                        #48bit
        b = float(abc[2])                                                                    #24bit
    except (IndexError, ValueError, TypeError):
        print('Ошибка ввода. Попробуйте снова.')
        continue
    if sign=="0":
        print('конец программы')
        break
    print("Результат = " + str(operation(sign, a, b).get(True)))

#64+24+48+24 = 160 bit



