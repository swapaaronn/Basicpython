def palimdrom(word):
	value=word[::-1]
	if name==value:
		return "numbar is palimdron"
	else:
			return "number is not palimdrom"



name=input("enter name")
print(palimdrom(name))