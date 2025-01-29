# collection of unique elements
# undoreed collection
# indexing not supported
# slicing not supported
# represented in {} with comma seprated (,) elements
# mutable in nature

my_set={'anam',10,20,'sayyed',30,40}
print(my_set)
print(type(my_set))
# output={'anam', 10, 20, 'sayyed', 30, 40}
# <class 'set'>

# INBUILT FUNCTION
# MAX()
# MIN()
# TYPE()
# LEN()
# ID()
# SUM()

s1={'anam','raj','rahul'}
s2={10,20,30,40.5,60}
print(max(s1),max(s2))
# output=raj 60
print(min(s1),min(s2))
# output=anam 10
print(type(s1),type(s2))
#  output=<class 'set'> <class 'set'>
print(id(s1),id(s2))
# output=2059163688448 2059163689568
print(len(s1),len(s2))
# output=3 5
print(sum(s2))
# output=160.5

# ----------------------------------------------------------------------------------------------------------------------------

# METHOD:-

# ADD()
s1.add(20)
s1.add(90)

print(s1)

# CLEAR()
s1.clear()
print(s1)
# output=set()


# COPY()
# UPDATE()
l1={10,20,30,40}
s1.update(l1)
print(s1)
# POP()
s1.pop()
print(s1)
# REMOVE()
s2.remove(20)
print(s2)

# s2.remove(20)-----------------error
# print(s2)
# DISCARD()
s2.discard(30)
print(s2)
s2.discard(30)
print(s2)
# -----------------------------------------------
# METHEMATICAL OPERATION
# UNION()
a={1,2,3,4,5,6}
b={3,6,7,8,9}
print(a.union(b))
# output={1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a)
# INTERSECTION()/INTERSECTION_UPDATE()
print(a.intersection(b))
# output={3, 6}
print(a)
# DIFFERENCE()/DIFFERENCE_UPDATE()
print(a.difference(b))
# output={1, 2, 4, 5}
print(a)
# output={1, 2, 3, 4, 5, 6}
print(a.difference_update(b))
print(a)
# SYMMETRIC_DIFFERENCE()/SYMMETRIC_DIFFERENCE_UPDATE()
a.symmetric_difference(b)
print(a)
b.symmetric_difference_update(a)
print(b)

# ISDISJOINT()
# ISSUBSET()
# ISSUPERSET()