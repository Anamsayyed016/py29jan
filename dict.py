# collection of key-value pairs
# Indexing not supported
# slicing not supported
# key must be a unique
# value may be duplicate
# represented in {} with comma seprated (,) elements
#  syn: d1={'key':'value','key2':value2,'key3':'value3'}

# inbuild function for dict. :

# MAX()
d1={'name':'anam','age':27,'quali':'Mba'}
print(max(d1))
# output=quali

# MIN()
print(min(d1))
# output=name

# LEN()
print(len(d1))
# output=2

# TYPE()
print(type(d1))
# output=<class 'dict'>


# ID()
print(id(d1))
# output=2499292749696
# ---------------------------------------------------------------------

# INBULID METHOD

# clear()
# d1.clear()
# print(d1)
# print(id(d1))
# output={}---empty

# COPY
d2=d1.copy()
print(id(d1),id(d2))
print(d1,d2)
# 2690462375808 2690462770176----diff. id
# output={'name': 'anam', 'age': 27, 'quali': 'Mba'} {'name': 'anam', 'age': 27, 'quali': 'Mba'}


# FORMKEYS()
# l1=['name','email','contact']
# d2=dict.fromkeys(l1)
# print(d2)
# output={'name': None, 'email': None, 'contact': None}----by default
# # d3=dict.fromkeys(l1,99)
# print(d3)
# output-{'name': 99, 'email': 99, 'contact': 99}

# GET()
print(d1.get('key'))
print(d1.get('name'))
# output=anam----access the key value

# ITEM()----output in tuple format
print(d1.items())
# output=dict_items([('name', 'anam'), ('age', 27), ('quali', 'Mba')])

# KEYS()
print(d1.keys())
# output=dict_keys(['name', 'age', 'quali'])

# VALUES()
print(d1.values())
# output=dict_values(['anam', 27, 'Mba'])


# POPITEM()
print(d1.popitem())
# output=('quali', 'Mba')
print(d1)
# output={'name': 'anam', 'age': 27}---remaining

# POP()
print(d1.pop('name'))
# output=anam
print(d1)
# output={'age': 27}

# SETDEFAULT
d1.setdefault('name','sayyed')
# output={'age': 27, 'name': 'sayyed'}
print(d1)

d1.setdefault('new','guest')
# output={'age': 27, 'name': 'sayyed', 'new': 'guest'}---create new key value paris
print(d1)

# uPDATE()
# output={'age': 27, 'name': 'anam', 'new': 'guest', 'quali': 'Mba'}
d1.update(d2)
print(d1)