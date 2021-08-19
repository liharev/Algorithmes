def place(letter):
    if letter < 1078:
        return (letter-1071)
    elif letter > 1078:
        return (letter - 1070)
    else:
        return(7)
while True:
    try:
        letter1, letter2 = map(ord, input("Введите две строчные буквы русского алвавита: ").split())
        if (((letter1 > 1071 and letter1 < 1104) or letter1==1105) and
            ((letter2 > 1071 and letter2 < 1104) or letter2==1105)):
            break
        print('Ошибка ввода. Попробуйте снова.')
    except TypeError:
        print('Ошибка ввода. Попробуйте снова.')
place1 = place(letter1)
place2 = place(letter2)
print(f"Буква {chr(letter1)} находится на {place1} месте, а {chr(letter2)} - на {place2}")
print("Между ними " + str(abs(place2-place1)-1) + " букв")