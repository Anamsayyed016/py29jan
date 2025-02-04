n=int(input("enter any no. "))
x=y=n
digit=0
while n>0:
    digit = digit+1
    n=n//10

sum=0
while y>0:
    last_digit = y%10
    sum=sum+last_digit**digit
    y=y//10

if x==sum:
    print(f'{x} is armstrong')

else:
    print(f'{x} is not armstrong')        

   
# print(digit)
# print(n)
# output=7
# 0