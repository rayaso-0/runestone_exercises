# Write a program that asks the user for three and prints the least of them.
num1 = float(input("Give me your first number: "))
num2 = float(input("Give me your second number: "))
num3 = float(input("Give me your third number: "))

if num1 < num2 and num1 < num3:
  print("Your first number", num1, "is the least out of the three")
elif num2 < num1 and num2 < num3:
  print("Your second number", num2, "is the least out of the three")
elif num3 < num1 and num3 < num2:
  print("Your third number", num3, "is the least out of the three")

# Write a program that asks a the user for a three-digit integer X consisting of three different digits, 
# and prints "YES" if its three digits are going in an ascending order from left to right and print "NO" otherwise.
num = int(input("Give me a three digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

numli = [hundreds, tens, ones]

if numli[0] < numli[1] and numli[0] < numli[2]:
  print("Yes, your number has ascending digits.")
else:
  print("No, your number does not have ascending digits.")

# Let's call an integer a palindrome if it remains the same after reading its digits from right to left. 
# Write a program that asks the user for a four-digit integer, and prints "YES" if it's a palindrome and prints "NO" otherwise.
palindrome = input("Give me a four digit number: ")

if palindrome == palindrome[::-1]:
  print("YES")
else:
  print("NO")

# Write a program that asks for a day number (1-7), and prints the day of the week ("Sunday", "Monday", etc.). 
# If an invalid day number is provided, return "Invalid". You can assume that the week starts with Sunday.
day = int(input("Enter a number corresponding to the day of the week (1-7): "))

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 1 <= day <= 7:
  print(week[day - 1])
else:
  print("Invalid")

# Write a program that asks the user for a given a month - an integer from 1 to 12, and prints the number of days in it in the year 2025.
month = int(input("Enter a number coresponding to a given month (1-12): "))


month_li = ["January", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if 1 <= month <= 12:
  print(f"The month you chose is {month_li[month - 1]} and it has {days_li[month - 1]} days!")
else:
  print("Please enter a valid input.")

# Write a program that asks the user for three integers and determines how many of them are equal to each other. 
# The program should display 3 (if all are same), 2 (if two of them are equal to each other and the third one is different) 
# or 0 (if all numbers are different).

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))

if num1 == num2 and num1 == num3:
  print(num1, ",", num2, ",",num3, "are all the same number.")
elif num1 == num2:
  print("Your first number:", num1, ", and your second number:", num2, ", are equal to each other.")
elif num1 == num3:
  print("Your first number:", num1, ", and your third number:", num3, ", are equal to each other.")
elif num2 == num3:
  print("Your second number:", num2, "and your third number:", num3, ", are equal to each other.")
else:
  print("None of your numbers are equal to each other.")

# Write a program that asks the user for a year number (e.g, 1999) and checks if this year is a leap year. 
# If it is, print LEAP, otherwise print COMMON.
# The rules in Gregorian calendar are as follows:
# - a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
# - a year is always a leap year if its number is exactly divisible by 400

year = int(input("Please enter your year of choice: "))

if year % 400 == 0:
    print("LEAP")
elif year % 4 == 0 and year % 100 != 0:
    print("LEAP")
else:
    print("COMMON")

# We are organizing a party that requires specific amounts of tea and cookies. 
# Write a program that helps determine if the quantities of tea and cookies are sufficient for the party. 
# The program should prompt the user to input two numbers, one for the amount of tea and one for the number of cookies and display one of the following messages:
# "bad" if either the amount of tea or cookies is less than 5, the party is considered bad
# "good" if both the amount of tea and cookies are at least 5, the party is considered good.
# "great" if the party is already good, and either the amount of tea or cookies is at least double the amount of the other, the party is considered great.

tea = int(input("How much tea is being brought?: "))
cookies = int(input("How many cookies are being brought?: "))

if tea < 5 or cookies < 5:
    print("bad")
elif tea >= 5 and cookies >= 5:
    if tea >= 2 * cookies or cookies >= 2 * tea:
        print("great")
    else:
        print("good")
