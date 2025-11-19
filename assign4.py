# The user enters a string containing a number (e.g.45 ). Convert it to: 
#                                                                     integer - float  - string
#                                                           Print all three values with their types


data=input("Enter a String:  ")

a = int(data)
b =float(data)
c = str(data)

print(a , b , c)
print(type(a) , type(b), type(c))