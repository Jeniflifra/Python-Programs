#Restaurant billing calculator (no.of items and total price)

print("Platez")
print("Nagercoil")
total=0
while True:
  print("1. Dosa")
  print("2. Poori")
  print("3. Idly")
  print("4. Coffee")
  print("5. Exit")
  choice=int(input("Enter your choice : "))
  match choice:
    case 1:
      print("Dosa")
      do=int(input("Enter number of dosa : "))
      total+=10*do
    case 2:
      print("Poori")
      poo=int(input("Enter number of poori : "))
      total+=15*poo
    case 3:
      print("Idly")
      id=int(input("Enter number of idly : "))
      total+=7*id
    case 4:
      print("Coffee")
      cof=int(input("Enter number of coffee : "))
      total+=12*cof
    case 5:
      print("__________________")
      print("Billing")
      print("Total price",total)
      print("__________________")
      break
