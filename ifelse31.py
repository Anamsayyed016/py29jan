x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3rd number:"))

if (x>y and x>z):
    print(f"{x} is greater")
else:
    if(y>z and y>x):
        print(f"{y} is greater")
    else:
        print("{z} is greater",z)
        # output:Enter 1st number:10
            # Enter 2nd number:20
            # Enter 3rd number:30
            # {z} is greater 30