def cub_finder(l):
    emp=dict()
    for i in range(1,l+1):
       emp[i]=i*i*i
    return emp
    
number=int(input("enter number"))
print(cub_finder(number))

# without function
'''num=dict.fromkeys(range(1,11),"unknow")
new ={}
for i in num:
      new[i] = i**3
print(new)
'''
