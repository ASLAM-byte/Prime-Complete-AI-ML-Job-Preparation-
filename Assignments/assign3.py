# Ask the user to enter two integers and one float. Convert them all to floats 
# and print their average. 

data=input("Enter two integers and one float - a b c : ")
parts=data.split()

a=float(parts[0])
b=float(parts[1])
c=float(parts[2])

Avg= (a+b+c)/3

print("Their Averageis: ", Avg)
