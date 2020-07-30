#fromkeys--> we can use this method to assign multipal value same output
#  in dictionaries
#formkeys method inside we can use tuple,list,string

x=dict.fromkeys(('name','age','college'),"unknow")
print(x)

c=dict.fromkeys(range(1,11),"unknow")
print(c)

y=dict.fromkeys(['name','age','college'],["om",26])
print(y)

z=dict.fromkeys("abc",[1,2,3,4])
print(z)


#get method--->

y=dict.fromkeys(['name','age','college'],["om",26])
print(y.get('name'))

print(y.get('namesssss'))

print(y.get('namesssss',"not foubd!!!"))
#clear method

y.clear()
print(y)

#copy method

y1=z.copy()
print(y1.popitem())


