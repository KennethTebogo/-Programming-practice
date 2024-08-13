########################################

### PRAC 2 ###

########################################

# Kenneth
# 3968676
# Don't forget to rename this file with your student number!
# For instance, my file would be named 1234567_prac4.py 
# Also don't forget to comment your code or you get no marks! 

########################################

### Question 1 ###

########################################

### Q1.1 

#This code convert 80 km/h to meters per second and print the result
print(80/3.6)
#result:22.22

### Q1.2 

#This code calculate the resistor of the current using potential differece and current. 
print(1.5/1e-3)
#result:15000

### Q1.3 

#This code calculate the density in kg per cubic meter.
print((200/1000)/(((3e-2)**2)*(10e-2)))
#result:2222.222222222222

### Q1.4 

#this code calculate the kinetic energy of the truck in joules. 
print(0.5*(1000*10)*(60/3.6)**2)
#result:1388888.8888888892

########################################

### Question 2 ###

########################################

### Q2.1 

# This code calculate the sum with. 
# Define the function to add two numbers
def addition(m, n):
    return m + n

# Define the numbers
m = 7
n = 26

# Call the function and print the result
result = addition(m, n)
print(result)

### Q2.2 

# This code returns the second letter of the input string 
def second_letter(input_string):
    
    #check the length of the string
    if len(input_string) < 2:
        return "Error: The input string is too short to have a second letter."
    return input_string[1]

# Example usage
result = second_letter("computational")
print(result)
result = second_letter("awesome")
print(result)


### Q2.3 

# This function calculates the velocity of a free-falling body t seconds after it has been released.

def free_fall_velocity(t):
   
    # Acceleration due to gravity in m/s^2
    g = 9.81  
    # Equation of motion.
    velocity = g * t
    return velocity

# Example usage
time_seconds = 3
result = free_fall_velocity(time_seconds)
print(f"The velocity of the body after {time_seconds} seconds is {result:.2f} m/s")
time_seconds = 39
result = free_fall_velocity(time_seconds)
print(f"The velocity of the body after {time_seconds} seconds is {result:.2f} m/s")

########################################

### Question 3 ###

########################################

### Q3.1 

# Put your code here 
# Define the variable x
x = int(input("Enter a number: "))  # Taking input from the user

# Check the value of x and print the corresponding message
if x > 0:
    #the value is positive.
    print("positive")
elif x < 0:
    #the value is negative.
    print("negative")
else:
    #the value is zero.
    print("zero")


### Q3.2 

# Put your code here 
# Define the string variable s
s = input("Enter a string: ")  # Taking input from the user

# Check the length of the string and print the corresponding message
if len(s) > 5:
    print("too long")
else:
    print("ok")


### Q3.3 

# Put your code here 
# Define the variable x
x = int(input("Enter an integer: "))  # Taking input from the user

# Initialize an empty list to store the divisors
divisors = []

# Check divisibility and append to the list if divisible
if x % 2 == 0:
    divisors.append(2)
if x % 3 == 0:
    divisors.append(3)
if x % 5 == 0:
    divisors.append(5)

# Print the results
if divisors:
    print("The number is divisible by:", ', '.join(map(str, divisors)))
else:
    print("not divisible by 2, 3 or 5")


########################################

### Question 4 ###

########################################

# Put your code here 
import numpy as np
from scipy.optimize import fsolve

# Define the function whose root we want to find
def func(x):
    return 10 - x * np.log(x)

# Initial guess for the root
initial_guess = 1.0

# Use fsolve to find the root
root = fsolve(func, initial_guess)

# Print the result
print(f"The root of the equation is approximately: {root[0]}")


########################################

########################################

