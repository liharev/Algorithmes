import random
num = random.randint(1,100)
res = False
for i in range(10):
    choice = int(input("Угадайте число от 1 до 100: "))
    if choice < num:
        print("Больше")
    elif choice > num:
        print("Меньше")
    else:
        print("Ага, угадали")
        res = True
        break
if res == False:
    print("Было загадано: " + str(num))