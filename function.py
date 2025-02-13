#  block of  reuseabilitiy code
# write one call multiple
# syn:-def--imp-- fun_name---imp----(parameter)---optional---- : ----imp | Declaration of  funtion
                        #   {body of fun}-----imp                        |
                        # return----optinal

                # var= fun_name--imp(argument---optional)----imp    | calling


# Type of funtion
# 1-In-build funtion-=max(),min(),len(),sum(),print(),input(),eval()

# 2-Uder-define funtion-=

# relation between parameter and arguement:-
# syn:- def sum(x,y)
    # return x+y
# print(y,x)
# print(p)
# -------------------------------------------------------
# 1- Positional arguement:-

# def fun_name(x,y):
#     return x+y

# z=fun_name(4,5)
# print(z)
# output=9

# Keyword Argument:-
# def fun_name(x,y):
   
#     print("value of x",x)
#     print("value of y",y)
#     return x+y
# p=int(input("Enter 1st value :"))
# q=int(input("Enter 2nd  value :"))
# z=fun_name(y=p,x=q)
# print(z)
# print (fun_name.__doc__)
# print(dir(fun_name))

# -----------------------------------------------------------------------
        #Default Argument:-

# def fun_name(x=0,y=0,z=0):
#     # p=x+y+z
#     # print("Hi")
#     print('x = ',x)
#     print('y = ',y)
#     print('z = ',z)

#     return x+y+z
# x=fun_name(4,5,6)
# # x=fun_name(4,5,6,7)

# # print(fun_name(1,2,3))
# # x=fun_name(5)

# print(x)

# ---------------------------------------------------------------------------------

# Variable Length Argument(* args----[for pas tuple][single star---all argument is not fix and asign with any name])

# def add (*n):
#     print(n)
#     print(type(n))
#     sum=0
#     for i in n:
#         sum=sum+1
#     return sum
# n=add(2,4,5,6)
# print(n)
    
# def add (*n):
#     print(n)
#     print(type(n))
#     sum=0
#     for i in n:
#         for x in i:
#             sum=sum+x
#     return sum
# p=eval(input("Enter any tuple :"))
# n=add(p)
# print(n)

# def add(*n):
#         sum=0
#         for i in n:
#                 sum=sum+i
#         return sum
#         # print(n)
#         # print(type)

# x=eval(input("Enter any value:"))
# y=add(*x)
# print(y)


# ---------------------------------------------------------------------------------------
# (**n(kwarg))
# variable keyword argument:-

def show_my_detail(**n):
        
        # for k,v in n.items():
        #         print(f' My {k} is {v}')

        print(n)
        print(type(n))

x=eval(input("Enter the value:"))
show_my_detail(**x)
# show_my_detail()
# show_my_detail(name='Anam',age=27,qualifi='MBA')
