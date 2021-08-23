strlenght = 0
output = ''
for i in range (96):
    output = output + str(i+32) + "-" + chr(i+32) + " "
    strlenght += 1
    if strlenght == 10:
        print(output)
        output = ''
        strlenght = 0
print(output)
