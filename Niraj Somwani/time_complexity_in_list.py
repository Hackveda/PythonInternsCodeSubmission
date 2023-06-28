#Creating a list
list1 = [1,2,3,4,5,6,7,8,9]
list1


#Append (it is used to add value in the end of list)
list1.append(10) #Time complexity is O(1)
list1


#Extend in list
list2 = [11,12,13,14,15] #K elements
list1.extend(list2)  #O(k) Time complexity
list1


#Calculation of time complexity in extend operation
list1 = [1,2,3,4,5,6,7,8,9,10]
list1
list2 = [11,12,13,14,15]
list2

#extend list1 with list2
for element in list2:
  list1.append(element)
list1 


#Insert in List
list1.insert(0,0)
list1.insert(17,16)
list1


#Remove item in list
list1.remove(0)
list1


#Pop in list
list1.pop(0)
list1


#clear the list
list1.clear()
list1


#Index operation in list
list2
list2.index(15)


#Extend operation in list
list3 = [15,15,17,20,19]
list2.extend(list3)
list3


#count the number of same items in list
list3.count(15)


#align item in ascending order
list3.sort()
list3


#align item in decending order
list3.sort(reverse=True)
list3


#Reversing of list
list4 =[2,3,43,4,5,32,12]
list4.reverse()
list4


#copy one list to another list
list5 = list3.copy()
list5
