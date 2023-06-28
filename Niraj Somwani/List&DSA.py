#List and Data Structure and Algorithm
#creation of list
myList = [1,2,3,4,5,6]
myList


#Searching in list
myList = [1,2,3,4,5,6]
searchItem = int(input("Enter your item "))
index = 0
for listItem in myList:
  if listItem == searchItem:
    print("Item found at index",index)
  else:
    print("Item is not found")  
    index = index +1 
