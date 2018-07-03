number = list(range(1,101))
sum1 = 0
sum2 = 0
for i in number:
    if i%2 != 0:
        sum1 = sum1 + i
    else:
        sum2 = sum2 + i
sum = sum1-sum2
print (sum)