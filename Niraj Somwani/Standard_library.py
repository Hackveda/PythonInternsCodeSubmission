#Standard Lib
#Command Line Argument
import sys
name = sys.argv[1]
age = sys.agrv[2]
height = sys.argv[3]
print("Command line Argument are",name,age,height)


#String pattern matching 
#Check if the email id is valid or not

import re
email = input("Enter Your Email ID ")
findEmail =re.findall(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$',email)
print(findEmail)
if len(findEmail) != 0:
  print("Email ID is valid")
else:
  print("Email ID is invalid")  
  
  
  
#Using random in Python
import random
myList = [0,2,4,6,8,10,12,14,16,18,20]
print("Random number is: ",random.choice(myList))  


#Implemented Dice using random
dice = [1,2,3,4,5,6]
print("Your value is: ",random.choice(dice)) 



#Implement Statistics in Python
import statistics
mystat = [5,34,76,0,9]
statistics.mean(mystat)


#Implementation of Data and Time
from datetime import date
today = date.today()
today.strftime("%d/%m/%y")


today.strftime("Day is %A (%a), Month is %B (%b)")



#Data compression in Python
import zlib
data = b"This is my code"
zlib.compress(data)



#Performance measurement in Py
import timeit
timeit.timeit("[i*2 for i in range(10)]")


#Quality control in py
def sum(a , b):
  """
  This function is used to sum of two number 
  >>> print(sum(20,30))
  50
  """
  return a+b

#testing the sum function
import doctest
doctest.testmod()



def sub(y , z):
  """
  This function is used to subtraction of two number 
  >>> print(sub(80,56))
  24
  """
  return y-z

#testing the sum function
import doctest
doctest.testmod()



#Multi Threading in Python
import threading

class MyOperation(threading.Thread):
  def __init__(self,a,b):
    threading.Thread.__init__(self)
    self.a = a
    self.b = b
  
  def run(self):
    print("Sum is ",self.a + self.b)

MyOperation(10,20).start()
print("GUI thread executed")    

