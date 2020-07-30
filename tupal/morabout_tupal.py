#in tupal we can't use pop(),insert(), remove(),append()
#only use count() and index()


#tupal in loop 
mixed=(1,2,3,4.0,5.0)
i=0
total=0

'''for i in mixed:
     total=total+i
     i=i+1
     print(total)
'''
while i<=len(mixed):
        total=total+i
        i=i+1
        print(total)     
 

#tupal without paranthesis
value="swapnil","mali","sanjay"
print(type(value))
   # OR
x="swa",    
print(type(x))


#tupal in side list
favorate=('swapnil','mali',[1,2,3,4,5,6])
favorate[2].pop()
favorate[2].append("56")
print(favorate)

# something more about us tupal ,list,str

num=tuple(range(1,12))
print(list(num))
print(str(num))

num_list=str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(num_list))
print(tuple(num_list))


#we can use method count and index ()
# we can use function  max(),min(),sum(),len()
maxvalue=(1,2,3,4,5,4,5,8,8,9,6,8)
print(maxvalue.count(8))
print(maxvalue.index(8,7))


print(len(maxvalue))
print(max(maxvalue))
print(min(maxvalue))
print(sum(maxvalue))
