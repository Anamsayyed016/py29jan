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
# 1- positional arguement:-

# def fun_name(x,y):
#     return x+y

# z=fun_name(4,5)
# print(z)
# output=9

# keyword Argument:-
def fun_name(x,y):
   
    print("value of x",x)
    print("value of y",y)
    return x+y
p=int(input("Enter 1st value :"))
q=int(input("Enter 2nd  value :"))
z=fun_name(y=p,x=q)
print(z)
print (fun_name.__doc__)
print(dir(fun_name))