#Fancier Output Formatting
#old method to print string
name = "Neeraj"
print("My name is: ", name)


#Method 1:
#new method to write formated string using (f or F) before opening quatation
name = "Neeraj"
surname = "Somwani"
statement = f"My name is {name} and surname is {surname}"
#After putting f before opening quote it will be variable
print(statement)


#Method 2:
#str.format() 
totalAmt = 23500
acHolder = "Niraj"
"Total amount of user:{} is {:,}$".format(acHolder,totalAmt)


#converted decimal value into octa, binaryand in hexa using format()
d_val = 10
"Binary value of {} is {:b}".format(d_val,d_val)

"Octa value of {} is {:o}".format(d_val,d_val)

"Hexa value of {} is {:x}".format(d_val,d_val)


#Reading and Writing Files in Python

with open("myinfo.txt") as f:
  myfile = f.read()
print(myfile)  


#reading each line
with open("myinfo.txt") as f:
  myline = f.readline()
print(myline)  


#to print all the line in document we use while loop for that
with open("myinfo.txt") as f:
  for line in f:
    print(line)
    
    
#Creating and writing in new file
with open("myaddress.txt", "w") as f:
  f.write("53, ITI")   
  
  
#Writing Json data in python
import json
data = {"Name":"Neeraj Somwani", "Age": 22}
json.dumps(data)  


#Wirte json data into a file
with open("Json.json","w") as f:
  json.dump(data,f)
