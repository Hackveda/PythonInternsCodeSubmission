#List in Python
#Personal info
name = "Neeraj"
age = 21
height =5.5
position = "developer"

#group all the info in compound data type
myinfo = [name,age,height,position]
myinfo


#checking for homogeneous and hetrogeneous data
for item in myinfo:
  print(item, type(item))
  
  
mylist = [2,4,6,8,10,12,14,16,18,20]
mylist
#random access of number
mylist[6]


#slice in list
mylist[1:8]


#List is mutable (change the existing value of list)
mylist[9] = 40
mylist
