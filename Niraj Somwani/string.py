#Using String 
name = "Niraj"
surname = "Somwani"
print(name , type(name))
print(surname ,type(surname))


#single quote and double quote String
statement1 = "Hello World!!"
statement2 = 'Hello World!!'
print(statement1)
print(statement2)


#Using single quote and double quote string in one variable
statement3 = "He doesn't understand"
print(statement3)

#Using the backslash to avoid the syntax error single quote string
statement4 = 'He doesn\'t understand'
print(statement4)

#Using backslash to avoid syntax error in double quote string
statement5 = "If you want to shine like a sun, first burn like a sun BY \"APJ\" Abdul Kalam Sir"
print(statement5)


#To avoid backslash escaping we can use r (raw string)
print('c:\\user\test')
print(r'c\\user\test')


#multiple line using triple double or triple single quote
print(""""This is 
the example
of Multiple line in python
using double quote \n""")

print('''This is the 
example of 
single line in python 
using single quote''')


#String concatenation (+)
string1 = "This is my first name 'Niraj' \n"
string2 = "This is my last name 'Somwani'"
string3 = string1 + string2 
print(string3)


#String Repetation (*)
alphabate = "P\t"
word = "Python\t"
statement = "This is python class \t"
print(alphabate*5)
print(word*5)
print(statement*2)


#String indexing (subscripting)
city = "VADODARA"
len(city)  #len() is used to find the size of string

print(city[0]) # String number always start with 0
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[5])
print(city[6])
print(city[7])


#negative index in string
print(city[-1])
print(city[-2])
print(city[-3])
print(city[-4])
print(city[-5])
print(city[-6])
print(city[-7])
print(city[-8])


#find character using positive and negative string indexing
Myname = "Neeraj"
print(Myname[3])
print(Myname[-3])

#slicing in string using index
slice = Myname[0:4]
print(slice)

print(Myname[3:6]);

print(Myname[-3:])
