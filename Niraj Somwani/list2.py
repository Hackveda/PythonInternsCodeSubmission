#Syntax of list is []
emptyList = []
print(type(emptyList))


#We need list to group the value togerther 
#the group may be homogenous and hetrogenous in list
#The list are considered as compound data type

student_id = [1,3,5,7,9,11,13,15,17,19]
student_id
print(type(student_id)) #this ia called homogenous list


#Hetrogenous list
student_name = "Raj"
student_age = 16
student_height = 5.2
print(student_name,type(student_name))
print(student_age,type(student_age))
print(student_height,type(student_height))

#Group abouve information in a grp
student_info = [student_name,student_age,student_height]
student_info


#finding the index of each item in a list
index = 0
for item in student_id:
  print(index,item)
  index = index + 1
  
  
index_no = int(input("Enter your index number: "))
print("The value at index" , index_no , "is" , student_id[index_no])


#Slicing using user input
inclusive = int(input("Enter inclusive number: "))
exclusive = int(input("Enter exclusive number: "))
student_id[inclusive:exclusive]


#Concatenation in list
student1 = ["Neer", 21, 5.6]
student2 = ["Raj", 18, 5.0]
conc_string = student1 + student2
conc_string


#Append in list
#it is used to add item in list
conc_string.append("7772023328")
conc_string


#update the list using the slice
newlist = ["Nick", 25 ,6.2]
conc_string[0:3] = newlist
conc_string


#remove the item in a list
conc_string[6:] = []
conc_string


#Calculate the size of list
print("The size of list is: ",len(conc_string))


#Nested list 
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
nested_list = [list1,list2,list3]
nested_list


#Access item from the nested list
nested_list[0][2]


list = [1,2,3,4,5,6,7,8,9]
list


#Insert the item at the top of list
list.insert(0,0)
list


#insert the item at the end od list
list.append(10)
list


#insert at specific location in the list
list.insert(6,5.5)
list
