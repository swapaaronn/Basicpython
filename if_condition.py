choice=int(input("""choice any one out of 3
 1.waterbill 			
2.electricitybill""")) 
if choice==1:
		billnumbar=int(input("enter bill number"))
billAmount=int(input("billamount"))
billpay=int(input("billpay")) 
if billpay==billAmount:
       print("thnak you for bill pay")
elif billpay<=billAmount:
       balancebill=billAmount-billpay
       #print("balance amount"+str(balancebill))
       print(f"balance amount{balancebill}")
       #print("balance amunt {}".format(balancebill)) 
elif choice==2:
       billnumber=int(input("enter electricity no."))
       billAmount=int(input("enter amount"))
       billpay=int(input("billpay"))
       if billpay==billAmount:
        print("thnak you full pay ment")
elif billAmount>=billpay:
       differce=billAmount-billpay
       print("balance amount {}".format(differce))
elif choice==3:
       print("enter property tax no.")
       
       
''' ege=int(input("enter age")) 
       if ege>=18:
       	print("ege more than 18")
       	else:
       		print("ege less than 18")
      ''' 