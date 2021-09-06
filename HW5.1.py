import collections
fnum = int(input("Введите количество компаний: "))
company = collections.namedtuple('company', 'name q1 q2 q3 q4')
flist = []
q = []
for i in range(fnum):
    name = input('Введите название компании: ')
    for j in range(4):
        q.append(int(input(f"Прибыль {name} в {j+1} квартале: ")))
    flist.append(company(name=name, q1=q[0], q2=q[1], q3=q[2], q4=q[3]))
    q.clear()
avgprofit = sum((x[1]+x[2]+x[3]+x[4]) for x in flist)/len(flist)
print(f"Средняя прибыль: {avgprofit}")
a = map(flist[0], flist)
print(f"Прибыль выше средней: {a}")
