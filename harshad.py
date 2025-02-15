n=int(input("Enter any number : "))
x=n
sum=0
while n>0:
    last_digit=n%10
    sum=sum+last_digit
    n=n//10
print(sum)
print(n)
if x%sum==0:
    print("harshad no")
else:
    print(" not harshad no")
