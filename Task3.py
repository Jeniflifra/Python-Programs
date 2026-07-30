#FizzBuzz

num=int(input("Enter the number - "))
for n in range(1,num+1):
    if(n%2==0):
      print("Fizz")
    elif(n%3==0):
      print("Buzz")
    elif(n==7):
       print("Seven")
    else:
       print(n)
