# scope of variable:
# 1.local scope
# 2.global scope
# x=10
# def add():
#     global y
#     y=20
#     print(x)
#     print(y)

# add()
# print(x)
# print(y)

# x=10
# def new():
#     global x
#     print(x)
#     x=20
#     print(x)
# new()
# print(x)

x=10
def new():
    global y,x
    x=20
    y=10
    print("Value of global variable x :",globals()['x'])
    print("Value of global variable x :",x)
new()
print(x)    
print(y)    