# Take two numbers as input from the user and print their sum, difference, 
# product, and quotient

data= input("Enter number1 number2 : ")
parts=data.split()

number1=float(parts[0])
number2=float(parts[1])

sum=number1+number2
diff=number1-number2
prod=number1*number2
quotient=number1/number2

print("Their Sum is: " ,sum ,   "Difference is:", diff ,"   Product is: ", prod ,"  Quotient is:", quotient)