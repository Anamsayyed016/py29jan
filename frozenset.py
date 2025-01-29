# collection of unique elements
# undoreed collection
# indexing not supported
# slicing not supported
# represented in {} with comma seprated (,) elements
# immutable in nature

s="anam"
l=[10,20,30,40]
t=(10,20,322,4,8)
d={'name':'anam','age':20}
s1={'anam','raj','rahul'}

x=frozenset(s)
print(x)
print(type(x))
# output=frozenset({'a', 'n', 'm'})
y=x.copy()
print(y)

# METHOD:-
a={2,4,6,8}
b={1,3,5,7,6,8}
x=frozenset(a)
y=frozenset(b)

# DIFFERENCE()
print(x.difference(y))
# output=frozenset({2, 4})

# SYMMETRIC_DIFFERENCE()
print(x.symmetric_difference(y))
# output=frozenset({1, 2, 3, 4, 5, 7})

# INTERSECTION()
print(x.intersection(y))
# output=frozenset({8, 6})

# UNION()
print(x.union(y))
# output=frozenset({1, 2, 3, 4, 5, 6, 7, 8})

# ISDISJOINT()
# a={2,4,6,10}
# b={1,3,5,7,8}
print(x.isdisjoint(a))
# output=False-----------------if no common element then false
print(x.isdisjoint(b))

# ISSUBSET()
x={1,2,3}
y={1,2,3,4,5,6,7,8,9}
print(x.issubset(y))
# output=True-----------------all elements of x are present in y

# ISSUPERSET()
print(y.issuperset(x))
# output=True-----------------all elements of x are present in y