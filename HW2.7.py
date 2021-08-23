n = int(input("Введите n: "))
s1 = 0
for i in range(n+1):
    s1 = s1 + i
s2 = int(n*(n+1)/2)
print(str(s1)+ ' = ', str(s2))
