#  Take a decimal number as input (like: 45.78 ) and output its: • integer part - 45 fractional part - .78 

deci = input("Enter decimal input: ")
parts=deci.split(".")

integer_part = parts[0]
fractional_part="."+ parts[1]

print("Integer Part is: ", integer_part )
print(" Fractional Part is: ", fractional_part)