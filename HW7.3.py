import random

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return (smaller, [v], bigger)

def top_k(L, k):
    print(len(L))
    v = L[random.randrange(len(L))]
    print(v)
    (left, middle, right) = partition(L, v)
    print(left, middle, right, k)
    if len(left) == k:   return left
    if len(left)+1 == k: return left + middle
    if len(left) > k:    return top_k(left, k)
    return left + middle + top_k(right, k - len(left) - len(middle))

def median(L):
    n = len(L)
    l = top_k(L, (n - 1)/ 2 + 1)
    return max(l)

m = random.randint(5,10)
a = [random.randint(-100, 100) for x in range(2*m+1)]
print(a)
print(median(a))