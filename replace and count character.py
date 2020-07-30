name,char=(input("enter name and charecter")).split(",")
#print("length name ",len(name))
print(f"length  {len(name)}")
print(f"charecter  {name.lower().count(char.lower())}")


#replace()

nae="swap"
print(nae.replace("swap" ,"swapnil"))



#find()

name="enter is any thing value is your is is "
print(name.find("is",7))
print(name.index("is",7))