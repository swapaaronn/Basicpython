# set is  unorder collection data type and unique
# set we can not stor list,tupal 
l={1,2,3,3,2,1,13,44,6,7,6,"string"}
print(l)
print(type(l))

# remove dublicate value in list
a=[1,2,3,3,2,1,13,8,9,8,23,24,6,7,6]
b=set(a)
c=list(b)
print(c)
print(type(c))
# or
# b=list(set(a))

#method add ,remove and dicard ,copy
l.add(99)
print(l)

l.remove(2)
print(l)

l.discard(2)
print(l)



s=l.copy()
print(s)
