#Buying new car in the car showroom and show their selected car and price details

print("---------CAR SHOWROOM---------")
print("1. Kia sonet - 100000/-")
print("2. Maruti swift - 90000/-")
print("3. Nexon - 95000/-")
print("4. Hyundai - 120000/-")
choice=int(input("Enter carchoice(1-4) : "))
if(choice==1):
      car = "Kia sonet"
      price = 100000
elif(choice==2):
      car = "Maruti swift"
      price = 90000
elif(choice==3):
      car = "Nexon"
      price = 95000
elif(choice==4):
      car = "Hyundai"
      price = 120000
else:
      print("Invalid choice!")
      exit()

print("Selected car = ",car)
print("Price : /-",price)
print("-----------------------")
Discount= input("Are you eligible for 5% discount (yes/no)? : ")
if Discount.lower()=="yes":
      final_price= price -(price*5/100)
else:
      final_price= price
print("Final_amount = ",final_price)
print("Thanks for visiting our showroom")