# coll. of elements in a single obj.
# ordered coll.
# indexing supp.
# slicing supp.
# immutable nature
# represent in () with  comma , sperated elements
#tuple  is faster as compare to list (due to immutable nature as well as less required space for creation) 

# import sys
# x=''
# print(sys.getsizeof(x))
# output-41
# y=[]
# print(sys.getsizeof(y))
# output-56

# z=()
# print(sys.getsizeof(z))
# output-40


l1=(10,20,30,54,22)
print(l1)
print(type(l1))
# output=(10, 20, 30, 54, 22)
# <class 'tuple'>

# INBULID FUNCTION IN TUPLE:
# ------------------------------------
l1=(10,20,30,54,22)
print(min(l1))
print(max(l1))
print(sum(l1))
print(id(l1))
print(type(l1))
# output=10
# 54
# 136
# 2481832967552
# <class 'tuple'>

# METHOD IN TUPLE:
# ---------------------------
# COUNT
print(l1.count(10))
# output=0
# INDEX
print(l1.index(10))
# output=1
print(l1[-1])