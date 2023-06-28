#Control Flow Statement
a,b,c,d = 0,1,2,3  #Assign mu;tiple value in single line
print("THe value of variable is",a,b,c,d)


#While loop
#fibonacci series
while a<10:
  print(a)
  a,b = b,a+b
  
  
#if else statement
#Grade system application
#91-100 =A , 81-90 =B , 71-80 =C , Below or equal 70= Fail

#take user input in int
marks = int(input("Enter Yours Makrs: "))

#Condition
if marks >= 91:
  print("Grade A")
elif marks >=81:
  print("Grade B")
elif marks >=71:
  print("Grade C")
else:
  print("Fail")
  
  
#Switch Implementation of if
#Banking Application

card = int(input("Enter Your Card Details: "))
print(""""
Select Your Option

1.Account Details
2.Account Statement
3.Manage Debit and Credit Card
4.Change PIN
""")

option = int(input("Enter Your Option "))

if option == 1:
  print("Your Account Details are...")
elif option == 2:
  print("Account Statement are...")  
elif option == 3:
  print("Manage Cards....")
elif option ==4:
  print("Chage PIN number") 
else:
  print("Give correct Option..")    
  
  
import queue
#For Statement in py
#Ticket office application

queue = ["Vivek","Dhaval","Neha","Nilesh"]

#Making tickets for all person in queue
for traveller_name in queue:
  print("Making ticket for traveller",traveller_name)
  print("Ticket issued for",traveller_name)
print("Having a safe and enjoyable Journey....")    


#Add all the items in basket with the character  C
basket = ["Burger", "Chess", "Apple", "Chocolate", "Cream",
         "Almond", "Milk", "Biscuit"]
items = []
for i in basket:
  if i[0] == "C":
    items.append(i)
items 


#Range function in py
for i in range(0,50,5):
  print(i)
  
  
#using sum() in range to make sum total of all number
for i in range(10,20,3):
  print("items",i)
print("Total of all number:")  
sum(range(10,30,3))


#making list of item in between range
list(range(0,100,10))


#Break statement
for i in range(10):
  print(i)
  if i == 5:
    break       #break is used to stop the loop at any condition
    
#continue statement
for num in range(2,20):
  if num % 2 ==0:
    print("Even Number: ",num)
    continue   #it is used to continue the loop at any condition
  print("Find the odd number: ",num) 
  
  
#Pass statement
country = ["Dubai","India","ShriLanka","China","Bangaladesh"]
for name in country:
  if len(name) == 5:
    print(name)
  else:
    pass  
