a = [x+2 for x in range(97)]                                        #40+8*97=816bit     + 24bit
b = [x+2 for x in range(7)]                                         #40+8*7=96bit       + 24bit
multiplicity = lambda x, y: 1 if x % y == 0 else 0                  #24+24 = 48bit
count = 0                                                           #24bit
for i in a:                                                         #24bit
    for j in b:                                                     #24bit
        if j > i:
            continue
        count = count + multiplicity(i,j)
print(count)

#1080bit