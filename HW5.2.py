import collections
n = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']  # все цифры
numbers = []                                                           # список для односимвольных операций
transfer = '00'                                                        # перенос разряда
for i in range(len(n)):
    for j in range(len(n)):
        numbers.append(n[i]+n[j])       # заполнение таблицы от 00 до FF для односимвольного сложения и умножения

def justify(lst,lenght):                # выравнивание списков для операции сложения, добавление лидирующего нуля
    for i in range(lenght):
        if i >= len(lst):
            lst.appendleft('00')
        else:
            if len(lst[i])<2:
                lst[i] = '0' + lst[i]

def digsum(x,y):                         # односимвольное 16-ричное сложение с переносом разряда
    global transfer
    calc = numbers.index(x) + numbers.index(y) + numbers.index(transfer)
    res = numbers[calc]
    if calc > 15:
        transfer = '0' + res[0]
    else:
        transfer = '00'
    return res[1]

def numsum(x,y):                         # многосимвольное 16-ричное сложение
    clist = collections.deque()
    for i in range(len(x)):
        clist.appendleft(digsum(x[i], y[i]))
    if transfer != '00':
        clist.appendleft(str(transfer[1]))
    return clist

def digmul(x,y):                         # односимвольное 16-ричное умножение
    global transfer
    calc = numbers.index(x) * numbers.index(y) + numbers.index(transfer)
    res = numbers[calc]
    if calc > 15:
        transfer = '0' + res[0]
    else:
        transfer = '00'
    return res[1]

def nummul(x,y):                        # многосимвольное 16-ричное умножение
    global transfer
    elist = collections.deque()
    for i in range(len(x)):             # заполнение списка результатами умножения цифр множителя y на множимое x
        dlist = collections.deque()
        transfer = '00'
        for j in range(len(y)):
            dlist.appendleft(digmul(x[i], y[j]))
        if transfer != '00':
            dlist.appendleft(str(transfer[1]))
        for k in range(i):
            dlist.append('0')
        elist.appendleft(dlist)
    for i in range(len(elist)):         # выравнивание результатов со сдвигом разряда
        justify(elist[i], max(len(l) for l in elist))
        elist[i].reverse()
    transfer = '00'
    for i in range(len(elist)-1):       # сложение, получение результата многосимвольного умножения
        elist[i+1] = numsum(elist[i], elist[i+1])
        elist[i+1].reverse()
        for j in range(len(elist)):
            justify(elist[j], max(len(l) for l in elist))
    for i in range(len(elist[-1])):
        elist[-1][i] = elist[-1][i][1]
    elist[-1].reverse()
    return elist[-1]

a, op, b = map(str, input("> ").split())  # ввод выражения
alist = collections.deque(a)
blist = collections.deque(b)

if len(blist) > len(alist):
    alist, blist = blist, alist

if op == "+":
    justify(alist, len(alist))
    justify(blist, len(alist))
    alist.reverse()
    blist.reverse()
    print(''.join(numsum(alist,blist)))
if op == "*":
    justify(alist, len(alist))
    justify(blist, len(blist))
    alist.reverse()
    blist.reverse()
    print(''.join(nummul(alist,blist)))