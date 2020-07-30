#find odd and even no using list

def exe1(l):
    odd=[]
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

        output=[odd,even]
    return output

x=[1,2,3,4,5,6,7,8,9,10]
print(exe1(x))