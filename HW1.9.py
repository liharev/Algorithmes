while True:
    try:
        nums = list(map(int, input("Введите три целых числа: ").split(maxsplit=3)[:-1]))
        break
    except ValueError or TypeError:
        print('Ошибка ввода. Попробуйте снова.')
nums.sort()
print(nums)
print("Среднее значение: " + str(nums[1]))

