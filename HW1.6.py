while True:
    try:
        letter = int(input("Введите номер буквы: "))
        if letter > 0 and letter < 34:
            break
        print('В алфавите 33 буквы. Попробуйте снова.')
    except ValueError:
        print('Ошибка ввода. Попробуйте снова.')
if letter < 7:
    print("Это буква: " + chr(letter+1071))
elif letter > 7:
    print("Это буква: " + chr(letter + 1070))
else:
    print("Это буква: ё")


