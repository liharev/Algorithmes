while True:
    try:
        n = int(input("Ввелите количество слагаемых: "))
        break
    except TypeError:
        print('Ошибка ввода. Попробуйте снова.')
res = 0
term = 1
for i in range(n):
    res = res + term
    term = term/2
print(f'Результат = {res}')


