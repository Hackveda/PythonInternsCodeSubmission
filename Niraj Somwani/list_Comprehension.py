#List Comprehension
#code without list Comprehension
square = []          #creating a list
for i in range(10):  #perform operation based on condition
    squares = i ** 2  #performing operation
    square.append(squares)
square   


#Code with List comprehension
compList = [i**2 for i in range(10)]
compList


#List comprehension with some complex calculation
[i**2 for i in range(10) if(i % 2) == 0]


#Matrix in list comprehensive
matrix = [
    [2,4,6,8],
    [3,6,9,12],
    [4,8,12,16]
]
[[row[i] for row in matrix] for i in range(4)]


#Del the statement in list
tryoutList = ["Niraj", "Vivek", "Jivansh"]
del tryoutList[1]
tryoutList


#Tuples and Sequence
myTuple = ("Niraj","Jay","Vivek","Jay","Ranbir")
myTuple

#Tuples are immutable are item store in tuple can't be modify
#Tuples support same value in it


#Tuples support multiple items assignment 
name, surname,age,height = ("Niraj","Somwani",22,5.5)
print("Name",name,"Surname",surname,"Age",age,"Height",height)


#Set, sets are using curly braces
myset = {"Mayank","Raj","Parth","Raj","Dhaval"}
myset   #Same item is remove from the set automatically


#Set Comprehension
compSet = {i*10 for i in range(10) if (i % 2) == 0 }
compSet


#Dictinaries {Key: Value}
mydict = {"Name":"Nick","Age":21}
mydict
#update Dictinaries
mydict["Name"] = "Niraj"
mydict
#Delete item from dectinaries
del mydict["Age"]
mydict



#loops on Dictinaries
myDict1 = {"Name":"Nick","Surname":"Jonas","Age":35,"Height":6.1}
for index, value in myDict1.items():
  print("Index is:",index, "And value is:",value)

  
  
#Enumerate function return index and value associate to it
myList = [10,20,30,40,50]
for index, value in enumerate(myList):
  print(index,value)  
  
  
#Zip 
actors = ["Vicky","Ranveer","Ranbir"]
actress = ["Katrina","Deepika","Aliya"]
for actor, actres in zip(actors,actress):
  print("The opposite Actress of:",actor, "is", actres)  
