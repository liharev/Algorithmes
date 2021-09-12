import collections
fnum = int(input("Введите количество компаний: "))
company = collections.namedtuple('company', 'name data')
flist = []
q = []
nt = collections.Counter(q1=0,q2=0,q3=0,q4=0)
for i in range(fnum):
    name = input('Введите название компании: ')
    for j in range(4):
        q.append(int(input(f"Прибыль {name} в {j+1} квартале: ")))
    flist.append(company(name=name, data=collections.Counter(q1=q[0],q2=q[1],q3=q[2],q4=q[3])))
    nt.update(flist[i].data)
    q.clear()
avgprofit = sum(nt.values())/len(flist)
print("Список компаний с прибылью больше средней:")
for i in range(fnum):
    if sum(flist[i].data.values())>= avgprofit:
        print(flist[i].name)
print("Список компаний с прибылью меньше средней:")
for i in range(fnum):
    if sum(flist[i].data.values())< avgprofit:
        print(flist[i].name)


