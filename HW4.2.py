import math
import time

def bit_sieve(n):
    if n < 2:
        return []
    bits = [1] * n
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if bits[i - 2]:
            for j in range(i + i, n + 1, i):
                bits[j - 2] = 0
    return bits

n = 2000

t1 = time.time()
i = 2
count = 1
while True:
    i += 1
    count += 1
    for j in range(2,i):
        if i % j == 0:
            count -= 1
            break
    if count == n:
        print(i)
        break
t2 = time.time()
print(t2-t1)

t3 = time.time()
sieve = bit_sieve(int(1.5 * n * math.log(n)) + 1)
i = 0
while n:
    n -= sieve[i]
    i += 1
print(i + 1)
t4 = time.time()
print(t4-t3)