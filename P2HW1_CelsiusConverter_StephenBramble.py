#Tell the user that this is a program to convert C to F
#Ask user for temperature in Celsius
#Convert the temperature that has been input into fahrenheit
#Display converted temperature for the user.

print ("C to F converter")

Celsius=float(input("Enter temperature in Celsius:"))

Fahrenheit = Celsius * 9/5 + 32
            
print ("The temperature in Fahrenheit is,",format (Fahrenheit, ".1f"))

input ("Press any key to terminate.")
