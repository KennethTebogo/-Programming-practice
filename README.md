Question 1: Programming practice
20 marks (5 marks per question)
We will start with some questions that get you to write some very simple python code. Remember, you must
include both the code and the answer to the question in your answer sheet. Don’t use a calculator, always use
python!
Here is an example question:
“Write a python program to calculate the number of seconds in a year (exclude leap years).”
Your solution should look like this:
# 60s in a minute, 60 minutes in an hour, 24 hours in a day, 365 days in a year.
print(1*365*24*60*60)
Result: 31536000

Notice how I included a comment to explain what I’m doing. You will get marks for commenting your code, try to
add a comment for every line of code to show you know what it does. Also notice how I include the output of my
code to show it gets the right answer. You’ll lose marks without the output but you’ll get no marks at all without
the code!

Questions:
Computational Physics 322
1. a) Write some python code that converts 80km/h into m/s.
b) Include the answer in your report.
2. a) Write some python code to calculate the resistance of a resistor with a potential difference of 1.5V across
it and a 0.1mA current running through it (hint: remember Ohm’s law?).
b) Include the answer in your report.
3. a) You find a rectangular object made of an unknown material. Its base is square, with a side measuring
3cm, and it has a length of 10cm and a weight of 200g. Use python to calculate the density of this object.
b) Include the answer in your report.
4. a) Write some python code to calculate the kinetic energy (in Joules) of a 10 tonne truck travelling at 60km/h.
b) Include the answer in your report.

Solutoin:
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


Question 2: Functions
15 marks (5 marks per question)
Let’s practice writing simple python functions. Functions are critical to writing good programs for two reasons:
they allow you to rerun code again and again without having to rewrite it and it allows you to abstract complicated
code, which becomes very important for bigger programs.
Here is an example question, similar to the previous but where I ask for a function:
“Write a function that takes as an input argument a number of years and calculates the number of seconds in those
years (exclude leap years).”
Your solution should look like this:
def convert_to_seconds(num_of_years):
# 60s in a minute, 60 minutes in an hour, 24 hours in a day, 365 days in a year.
return num_of_years*365*24*60*60
This time, I can call my function as many times as I want for different inputs. For each question, I will ask you to
test your function with a few inputs.
Remember to comment your code and include the output for the test inputs I give you.
Questions:
1. a) Write a function that takes two input arguments, m and n, and returns m + n.
b) Test your code for m = 7 and n = 26 and include the answers in your report.
2. a) Write a function that takes a string as an input argument and returns the second letter of the string.
b) Test your code for “computational” and “awesome” and include the answers in your report.
3. a) Write a function that takes time, t, as an input argument and returns the velocity of a freefalling body t
seconds after it has been released. Assume no air resistence and zero initial velocity.
b) Test your code for 3s and 39s and include the answers in your report.

Solution:
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

Question 3: Conditional statemets
15 marks (5 marks per question)
These questions focus on the concept of if statements. If statements are critical in any program as they allow a computer to make a decision based on some input. Here is a good tutorial on if statements: https:
Computational Physics 322
//realpython.com/python-conditional-statements/
Remember for each question, you must include both the well-commented code and the answer to the question in
your answer sheet.
Questions:
1. a) Write a python program that checks a variable, x: it should print “positive” if x is greater than zero,
“negative” if less than zero and “zero” if it is exactly equal to zero.
b) Test your code for 7, -3 and 0 and include the answers in your report.
2. a) Write a python program that checks the length of a string, stored in a variable called s. If the string is
longer than 5 characters, print “too long”. Otherwise, print “ok”.
b) Test your code for the strings “cosmological” and “ohm” and include the answers in your report.
3. a) Write a python program to check if a variable, x, is divisible by 2, 3 or 5. If it is divisible by more than
one of these numbers, print all the numbers out of 2, 3 and 5 that it is divisible by. If it is not divisible by
any of them, print “not divisible by 2, 3 or 5”. Assume x is an integer.
b) Test your code for 12, 7 and 60 and include the answers in your report.

Solution:

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

Question 4: Root finding
5 marks
Use python to find the roots (https://www.britannica.com/science/root-mathematics) of the following equation:
f(x) = 10 − xln(x) = 0
You may solve this problem any way you choose. I recommend starting with the built-in scipy solver called “fsolve”.
You’ll get some marks if you can use it successfully. You’ll get more marks if you can write your own root-solver
from scratch. Even if this seems daunting, give it a try! The simplest approach involves looping1 over a range of
possible values until you find one close to zero...

Solution:

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
