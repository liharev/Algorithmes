while True:
    try:
        abc = int(input("Введите трехзначное число: "))
        check = abc/1000
        if check > 0.099 and check < 1:
            break
        print('Вы ввели не трёхзначное число. Попробуйте снова.')
    except ValueError:
        print('Вы ввели не трёхзначное число. Попробуйте снова.')
print("Сумма чисел "+str(abc)[0]+", "+str(abc)[1]+" и "+str(abc)[2]+" равна "+
      str(int(str(abc)[0])+int(str(abc)[1])+int(str(abc)[2])))
print("А произведение "+str(abc)[0]+", "+str(abc)[1]+" и "+str(abc)[2]+" равно "+
      str(int(str(abc)[0])*int(str(abc)[1])*int(str(abc)[2])))

