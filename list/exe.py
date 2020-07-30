def value(l):
    l[::-1]      
   # l.reverse()              
    return l
number=[2,3,4,5]
word=["world1","world2"]
print(value(number))
print(value(word))


def value2(l):
    emp=[]
    for i in range(len(l)):
        popped=l.pop()
        emp.append(popped)
    return emp

number=[1,2,3,4]
print(value2(number))