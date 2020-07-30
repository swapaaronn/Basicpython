# defind function take 2 input and common output

def exe2(l,k):
    empty=[]
    for i in l:
        if i in k:
            empty.append(i)
    return empty

value1=[1,2,3]
value2=[1,2,3,4,8]
print(exe2(value1, value2))