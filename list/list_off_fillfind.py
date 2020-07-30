new=["file.py","name.py","a.txt","b.py"]
for em in new:
	if em.endswith('.py'):
		print(em)
	
#add in list value

new=["mango","apple",55]
new.append("banana")
print(new)
new.insert(2,44)
print(new)
new.remove("mango") #remove()
print(new)
new.pop()              #delete last value in list if doesnot mention value in methid
print(new)

del new[2]                       #delete()

print(new)

