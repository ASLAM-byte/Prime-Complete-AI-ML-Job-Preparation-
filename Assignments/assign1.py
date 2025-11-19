# Write a program that asks the user for their name and age, then prints a 
# sentence like Hello Shradha, you are 21 years old! 

data = input( "enter your name age:  ")
parts=data.split()

name=parts[0]
age=parts[1]


print("Hello", name + ", you are", age, "years old!")
