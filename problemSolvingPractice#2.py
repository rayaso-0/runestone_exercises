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
