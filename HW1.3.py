def sign(num):
    return "-" if num<0 else "+"
while True:
    try:
        x1, y1 = map(int, input("Введите координаты первой точки: ").split())
        x2, y2 = map(int, input("Введите координаты второй точки: ").split())
        break
    except ValueError:
        print('Ошибка ввода. Попробуйте снова.')
k=(y2-y1)/(x2-x1)
b=x1*(y2-y1)/(x2-x1)+y1
print("Уравнение прямой по двум точкам: y = "+str(k)+"x"+sign(b)+str(abs((x1*(y2-y1)/(x2-x1)+y1))))