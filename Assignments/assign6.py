# Write a program to swap values of two numbers entered by the user.

a = input("Enter number1: ")
b = input("Enter number2: ")

print("Before Swapped: ", a , b)

a , b = b, a

print("After Swapped: ", a , b)
