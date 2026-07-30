#/movie booking in theatre and checking children's ticket, movie timing and discount is available for the price is above 500

Theatre_name= input("Enter theatre name - ")
Movie_name= input("Enter movie name - ")
Movie_time= int(input("Enter movie time - "))
Number_of_tickets= int(input("Enter no. of tickets - "))
Ticket_price= 130
Total_ticket_price= Ticket_price * Number_of_tickets
Child= int(input("Enter children age - "))
print("____________________________")
if(Child>5):
    Total_ticket_price= Total_ticket_price + Ticket_price
    print("Children also has to pay ticket price")
else:
    Total_ticket_price= Total_ticket_price - Ticket_price
    print("Children has no ticket price")
print("____________________________")
if(Movie_time==3):
    print("Movie is started")
else:
    print("Movie delayed (Before or after)")
print("____________________________")
print("Total ticket price : ",Total_ticket_price)
if(Total_ticket_price>500):
    print("Discount is applied")
else:
    print("No discount is applied")
