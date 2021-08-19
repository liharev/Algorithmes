def check(s1,s2,s3):
    if s1 < s2+s3:
        return (True)
    else:
        return (False)
def shape(s1,s2,s3):
    if (s1 == s2) and (s2 == s3):
        return("равносторонний")
    elif (s1 == s2) or (s2 == s3) or (s3 == s1):
        return("равнобедренный")
    else:
        return("разносторонний")
while True:
    try:
        side1, side2, side3 = map(float, input("Введите длины сторон треугольника: ").split())
        break
    except TypeError or ValueError:
        print('Вы ввели не числа. Попробуйте снова.')

if check(side1,side2,side3) and check(side3,side1,side2) and check(side2,side3,side1):
    print("Это " + shape(side1,side2,side3) + " треугольник")

else:
    print("Такого треугольника не существует")