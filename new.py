'''import random
user_number=int(input("enter winning numbar"))
winning_number=random.randint(1,100)
if user_number==winning_number:
	print("you are winn",user_number)
else:
	print("you are near winning nu.",user_number)
'''
winning=55
guess=1
value=int(input("enter winning value"))
while True:
	 if (winning==value):
		 print(f"you {guess}")
		 break
	
	 else:
		 if (winning>value):
			 print("value if low")
		 else:
			 print("vlaue if high ")
	
guess=guess+1

value=int(input("enter winning value"))

	