# Lab7
# Author: Justin Hoang


## add in functions from test.py's test statements here to make the pytest work
## Use this file and your test plan to complete the lab

def main():
    pass


if __name__ == "__main__":
    main()
def calculate_rectangle_area(length, width):
    return length * width

def calculate_hypotenuse(side1, side2):
    return (side1**2 + side2**2)**0.5

def is_even(number):
    return number % 2 == 0

def find_maximum(num1, num2):
    return max(num1, num2)

def grade_calculator(score):
    if score > 100 or score < 0:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


