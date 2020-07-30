user1=dict(name="swapnil"
,age=25,
college="imcot",
favorate=["swapnil",25,"imcot"],movie={"movie":"coco"})

# check if  key exist in  dictionaries
'''
if 'name' in user1:
    print(" present")
else:
     print(" not present")
'''
# check if value exite in dictionaries   ------->values()
if 25 in user1.values():
    print(" present")
else:
     print(" not present")


#loop if dictionaries
'''
for i in user1:
    print(i)        #----------> get all key
    print(user1[i]) #----------> get all value
'''
# Item method

for key,value in user1.items():  #------------->Item method
    print(f"key is {key} and value is {value}")
    