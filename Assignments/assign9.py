# Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and 
# compute simple interest

data = input("Enter Principal (P), Rate (R), Time (T) : ")
parts=data.split()

P = float(parts[0])
R= float(parts[1])
T= float(parts[2])

Simple_interest = (P * R * T)/100
print("Simple Interest is: " , Simple_interest)
