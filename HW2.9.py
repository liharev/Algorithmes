def keyfunc(item):
    return item[1]
lst = list()
while True:
    num = int(input("Введите натуральное число (0 - выход): "))
    if num == 0:
        break
    digs = [int(item) for item in list(str(num))]
    elem = [num, sum(digs)]
    lst.append(elem)
lst.sort(key=keyfunc)
print(lst[-1])

