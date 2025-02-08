x=int(input("Enter 1st Value :"))
y=int(input("Enter 2nd Value :"))

max_no=max(x,y)

while True:
    if max_no%x==0 and max_no%y==0:
        break
    max_no=max_no+1
print(f'LCM of {x} and {y} is {max_no}')