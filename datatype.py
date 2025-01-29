# datatype
# numeric- integer, float, complex

# string              
# list-----Collection of obj.
# tuple
# dict--- maped data type
# set
# frozenset
# boolean

# collection
# ordered ------ string, list, tuple, dict
# unordered-------set, frozenset---its hold unqiue content-- can not use duplicate content.
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Numeric-
# Integer:-
# x=10
# y=20
# print(type(x))
# print(type(y))
# z=x+y
# print(type(z))
# output-<class 'int'>
# <class 'int'>
# <class 'int'>

# x=10
# y=20
# print(type(x))
# print(type(y))
# z=x-y
# print(type(z))

# x=10
# y=20
# print(type(x))
# print(type(y))
# z=x*y
# print(type(z))
# print(type(z))

# x=10
# y=20
# print(type(x))
# print(type(y))
# z=x/y
# print(type(z)) 
# output-<class 'float'>
# .........................................................................

# Float

# x=10.5
# y=20.5
# print(type(x))
# print(type(y))
# z=x+y
# print(type(z))

# x=10.5
# y=20.5
# print(type(x))
# print(type(y))
# z=x-y
# print(type(z))

# x=10.5
# y=20.5
# print(type(x))
# print(type(y))
# z=x*y
# print(type(z))

# x=10.5
# y=20.5
# print(type(x))
# print(type(y))
# z=x/y
# print(type(z))

# output-<class 'float'>
# ------------------------------------------------------------------------------------------

# complex

# x=10.5+3j
# y=20.5+5j
# print(type(x))
# print(type(y))
# z=x/y
# print(type(z))
# output-<class 'complex'>
# -------------------------------------------------------------------------------------------------

# 2.String:

# s1='Python'
# print(type(s1))
# output-<class 'str'>

# in-build function:

# print()
# s1='Python'
# print(type(s1))
# output-<class 'str'>

# input()
# x=input("enter your name :")
# print(x)
# print(type(x))
# output-anam
# id()

# x=input("enter your name :")
# print(x)
# print(id(x))
# output-anam
# 3019095911776

# max()
# s1='python'
# print(max(s1))
# output-y

# min()
# s1='python'
# print(min(s1))
# output-h

# len()
# s1='python'
# print(len(s1))
# output-6

# diffe between function and method

# Method:
# lower()
# upper()
# title()
# capitaliza()
# find()
# index()
# join()
# spilt()

# str1="I love python"                
# print(str1.lower())
# print(str1.upper())
# print(str1.title())
# print(str1.capitalize())
# print(str1.swapcase())
# output= i love python
# i love python
# I LOVE PYTHON
# I Love Python
# I love python
# i LOVE PYTHON

# print(str1.index('z')) -----------error
# print(str1.find('P'))
# output=-1
# print(str1.find('z'))
# output=-1= 
# the diff. between index and find is index is geneate ERROR and index provide -1

# print(str1.split())
# ['I', 'love', 'python']---return in list form---by default spilt through space

# print(str1.split('o'))
# output=['I l', 've pyth', 'n']

# print(str1.split('o',1))
# output=['I l', 've python']
# -------------------------------------------------------------------------------------------------

# Join
# li=['Anam','Sayyed','Bhopal']
# print('*'.join(li).split('p'))
# # output=['Anam*Sayyed*Bho', 'al']
# x=','.join(li)
# output=Anam,Sayyed,Bhopal--------single obj. output
# print(type(x))
# output=<class 'str'>
# --------------------------------------------------------------------------------------------------

# Count
# print(str1.count('o'))
# output=2
# --------------------------------------------------------------------------

# List
# inbulit function for list
# l1=[10,10.4,'Anam',5,7,65]
# l2=[40,52,5,36,3,41]
# print(max(l2))
# print(min(l2))
# print(sum(l2))
# print(len(l1))

# print(id(l1),id(l2))
# print(type(l1),id(l2))
# ------------------------------------------------------------------------------

# Method

# append() - add one obj. at last position
# x=(10,20,30,40)
# l1=[10,10.4,'Anam',5,7,65]
# l1.append(x)
# print(l1)
# output=[10, 10.4, 'Anam', 5, 7, 65, (10, 20, 30, 40)]

# x=10
# l1.append(x)
# print(l1)
# output=[10, 10.4, 'Anam', 5, 7, 65, (10, 20, 30, 40), 10]

# x='Sayyed'
# l1.append(x)
# print(l1)
# [10, 10.4, 'Anam', 5, 7, 65, (10, 20, 30, 40), 10, 'Sayyed']

# x=[10,52,20]
# l1.append(x)
# print(l1)
# [10, 10.4, 'Anam', 5, 7, 65, (10, 20, 30, 40), 10, 'Sayyed', [10, 52, 20]]

# sort() - arrenge assending form

# extend()- add multiple obj. in last position.
# x=[1,2,3]
# l1.extend(x)
# print(l1)
# output= # [10, 10.4, 'Anam', 5, 7, 65, (10, 20, 30, 40), 10, 'Sayyed', [10, 52, 20], 1, 2, 3]

# insert()- add 1-obj. from required position

# l1.insert(0,'bhopal')
# l1.insert(x)
# print(l1)
# output=['bhopal', 10, 10.4, 'Anam', 5, 7, 65, (10, 20, 30, 40), 10, 'Sayyed', [10, 52, 20], 1, 2, 3]

# sort()-
# l1=[10,5,7,65]
# l1.sort()
# print(l1)
# output=[5, 7, 10, 10.4, 65]

# pop()- remove one-obj. from last postiton.
l1=[10,20,8,20.5]
l1.pop()
print(l1)
# output-[10, 20, 8]

# remove()- remove one-object from required pos.
l1.remove(20)
print(l1)
# output=[10, 8]
# reverse()-to arrenge in reverse order.
# l1.reverse()
# print(l1)
# clear()- remove all obj. from list.
l1.clear
print(l1)
# copy()- create another obj. with samne content.
# l1=[10,20,8,20.5]
l1=[10,20,8,20.5]
l2=l1.copy()
print(l1,l2)
print(id(l1),id(l2))
# count()- frequency
# l2=[50,7,52,41,50]
# print(l2.count())
# index()-obj. 
# print(l2.index(7))
print(l2.index(8))
# del()- delete collection
# del l1
# print(l1)






