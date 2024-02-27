# Lab5
# Author: Justin Hoang
from typing import Union
import random
from math import floor

"""_summary_
This lab is designed to get you familiar with Python Functions, parameters, return values, Type Hinting, and Docstrings.

Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.
"""
# 1. Write a function called number_squared(num) that takes a number as a parameter and prints out the number squared. Include Type Hinting and a Docstring.
def number_squared(num: Union[int, float]) -> None:
    print(f"The square of {num} is {num ** 2}")

# 2. Write a function called string_counter(str) that take a string as a parameter and tell you how many letters are in the string. Include Type Hinting and a Docstring.
def string_counter(string: str) -> int:
    return len([char for char in string if char.isalpha()])

# 3. Write a function called string_repeater(str, num) that takes a string and a number as parameters and prints out the string repeated that many times. Include Type Hinting and a Docstring.
def string_repeater(string: str, num: int) -> None:
    print(string * num)

# 4. Write a function called number_adder(num1, num2) that takes two numbers as parameters and returns the sum of the two numbers. Include Type Hinting and a Docstring.
def number_adder(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2

# 5. Write a function called jacket_checker(temp, raining) that takes in a temperature (int) and whether it is raining (bool) as parameters and prints out whether you should wear a jacket or not. If the temperature is above 60 Degrees and it is not raining you should return not to wear a jaket. Return a String "Wear a Jacket" or "Do not wear a Jacket".  Include Type Hinting and a Docstring.
def jacket_checker(temp: int, raining: bool) -> str:
    if temp > 60 and not raining:
        return "Do not wear a jacket"
    else:
        return "Wear a jacket"
# 6. Write a function def user_jacket_decision() -> str: that asks the user for a temperature and whether it is raining and then calls the jacket_checker function to tell the user whether they should wear a jacket or not. Your returned value should be the output of jacket_checker. Include Type Hinting and a Docstring.
def user_jacket_decision() -> str:
    temp = int(input("Enter the temperature: "))
    raining = input("Is it raining? (yes/no): ").lower() == "yes"
    return jacket_checker(temp, raining)
# 7. Import the random module and write a function called random_number() that returns a random number between 1 and 10. Include Type Hinting and a Docstring.
def random_number() -> int:
    return random.randint(1, 10)
# 8. Import floor from the math module (using from <module> import <function>) and write a function called round_down(num) that takes a number as a parameter (float) and returns the number rounded down to the nearest whole number. Include Type Hinting and a Docstring.
def round_down(num: float) -> int:
    return floor(num)
print(string_counter("Hello World!"))
string_repeater("Python", 3)
print(number_adder(5, 7))
print(jacket_checker(70, False))
print(user_jacket_decision())
print(random_number())
print(round_down(7.8))