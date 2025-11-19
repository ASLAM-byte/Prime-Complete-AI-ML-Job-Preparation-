# Ask the user for a temperature in Celsius (string input). Convert it to , 
#                                   then calculate and print temperature in Fahrenheit. 
# Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32

temp = float(input("Enter temparature in Celsius (String Input): "))

fahrenheit=(temp * (9/5)) + 32
print("Your temparature in Fahrenheit is :" , fahrenheit)
