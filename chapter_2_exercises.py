# ---------------------
# Chapter 2 Exercises that have some value to remember
# Tue Sep 10 
#----------------------

# Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.

time = int(input("What is the current time?: "))
alarm = int(input("Now how long do you want your alarm to be?: "))

final_time = (time + alarm) % 24

print(final_time)

# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.

day = int(input("What day are you leaving for your trip?: ")) 
length = int(input("How long will your stay be?: "))

final_day = (day + length) % 7

print(final_day)

# Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.

A = "All" 
B = "work" 
C = "and" 
D = "no" 
E = "play"
F = "makes" 
G = "Jack" 
H = "a" 
I = "dull" 
J = "boy."

print(A, B, C, D, E, F, G, H, I, J)

# Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.
P = 10000
n = 12
r = 0.08

t = int(input("How many years do you plan on holding?: "))
            
output = P * ( ((1 + (r/n)) ** (n * t)) )
            
print("The final amount after ", t, " years is", output)

# Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

pi = 3.14159
r = int(input("What is the radius of the circle?: "))

area = pi * (r ** 2)

print("The area of the circle with a radius of", r, "is", area)


