# while True:
#     print("1.Add\n 2.Sub\n 3.Multi\n 4.Div\n 5. OFF") 

#     n=int(input("Enter your choice : "))
#     if n==1:
#         x=int(input("Enter 1st Value :"))
#         y=int(input("Enter 2nd Value :"))
#         z=x+y
#         # print('Addition is = z')
#         print(f'Addition of {x} and {y} is {z}')

#     elif n==2:
#         x=int(input("Enter 1st Value :"))
#         y=int(input("Enter 2nd Value :"))
#         z=x-y
#         print(f'Addition of {x} and {y} is {z}')


#     elif n==3:
#         x=int(input("Enter 1st Value :"))
#         y=int(input("Enter 2nd Value :"))
#         z=x*y
#         print(f'Addition of {x} and {y} is {z}')


#     elif n==4:
#         x=int(input("Enter 1st Value :"))
#         y=int(input("Enter 2nd Value :"))
#         z=x/y
#         print(f'Addition of {x} and {y} is {z}')


#     elif n==5:
#         break
#     else:
#         print("please enter valid number")


# ______________________________________________

while True:
    print("1.Add\n 2.Sub\n 3.Multi\n 4.Div\n 5. OFF") 
    n=int(input("Enter your choice:"))
    p=(1,2,3,4)
    
    if n in p:
        x=int(input("Enter 1st Value :"))
        y=int(input("Enter 2nd Value :"))

        if n==1:
            z=x+y
            print(f'Addition of {x} and {y} is {z}')

        elif n==2:
            z=x-y
            print(f'sub of {x} and {y} is {z}')

        elif n==3:
            z=x*y
            print(f'mul of {x} and {y} is {z}')

        elif n==4:
            z=x/y
            print(f'div of {x} and {y} is {z}')
    
    elif n==5:
        break

    else:
        print("please enter valid number")
    
    
