sum = 0
temp = 0

for x in range(1, 11):
    if (x % 5==0) or (x % 7==0):
        continue
    else:
        sum = x + sum

print(sum)

print(1+2+3+4+5+6+7+8+9+10)