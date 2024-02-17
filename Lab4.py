# Lab4
# Author: Justin Hoang

"""_summary_
This lab is designed to get you familiar with Python Boolean Expressions, Conditional Expressions, if-elif-else statements, and while / for loops.
"""

# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 2. Write some code that asks the user for a number and prints out whether it is even or odd.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.
number = int(input("Enter a number: "))
count = 1
while count <= number:
    print(count)
    count += 1

# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.
total = 0
for i in range(5):
    num = float(input("Enter a number: "))
    total += num
average = total / 5
print("Average:", average)
# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.
for i in range(1, 11):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".
number = int(input("Enter a number for countdown: "))
while number > 0:
    print(number)
    number -= 1
print("Blast off!")
# 7. Write some code that asks the user for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print "Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i > 100:
        break
    if i % 7 == 0:
        print("Lucky")
