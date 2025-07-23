num=877
steps=0
while num>=10:
    temp=num
    sum_digit=0
    while temp > 0:
        sum_digit += temp%10
        temp=temp//10
    num=sum_digit
    steps+=1
print(steps)
