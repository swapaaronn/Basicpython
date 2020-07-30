def greater(a,b,c):
	if a>b and b>c:
		return a
	elif b>c and b>a:
		return b
	else:
			return c
first=int(input("enter no."))
second=int(input("enter no."))
third=int(input("enter no."))
print(greater(first,second,third))