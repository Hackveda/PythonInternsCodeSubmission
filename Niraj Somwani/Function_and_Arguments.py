#Function and Arguments in Python
#difine the function 
def functionName(paramter):
  "Document String for the function"
#Call the function
functionName(23)


#Method1: Defining function to add two numbers and return the value
def add(a,b):
  """Add two numbers and return the value
     for example: a=5 , b=9
     add(5,9)=14
  """
  return a+b
print("Addition of two number is",add(87,95)) 


#Method2: Defining the function to add number but not return the value
def add1(a,b):
  "Add of two numbers but not return value"
print("The addition of two number is",add(78,65))


ans1 = add(87,95) #return is used to store the value in variable
ans2 = add1(78,65) #noreturn cannot store the value and it gives none to the user
print(ans1)
print(ans2)


#Default arguments values(number of arguments are not defined)
#make a application to add new admission

def newAdmission(studentName,studentClass="Class 10",
                 studentGroup="Yellow"):
  "Function to add new student in a class"
  print("Student Added", studentName,studentClass,
        studentGroup)

#First way Call the function with no parameter
newAdmission()


#Second way is to give the position Arguments
newAdmission("Niraj Somwani")


#Third way is to give the parameter name
newAdmission("Vivek",studentGroup="Blue")


#Defining the Arguments list

#Create an application to make a cricket team and add players info
def iplTeam(teamName, *players):
  "Create a IPL team and players name in it"
  player_list =[]
  for player in players:
    player_list.append(player)
  print("IPL tems:", teamName,"Players Name:",player_list)
iplTeam("CSK","MS Dhoni","Ravindra Jadega","Suresh Raina","DJ Bravo")  


def iplPlayers(**players):
  for player in players:
    print("Player Name:", player,"Role:",players[player])
iplPlayers(Dhoni="Batter",Jadega="All rounder") 
