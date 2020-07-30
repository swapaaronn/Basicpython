# print how many list in program
def typelist(l):
    count=0
    for i in l:
        if type(i)==list:
            count=count+1
    return count

num=[2,4,5,6, [1,3],[5,7]]
print(typelist(num))
