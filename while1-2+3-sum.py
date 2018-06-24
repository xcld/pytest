a=0
sum=0
while a < 100:
    a+=1
    b=a % 2
    if b ==1:
        sum=sum+a
else:
    sum=sum-a
print(sum)