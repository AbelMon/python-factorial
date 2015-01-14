"""This program calculates a Fibonacci number"""
import os

def fib(number):
    """Generates a Fibonacci number."""
    if number == 0:
        return 0
    if number == 1:
        return 1
    total = fib(number-1) + fib(number-2)
    return total


def typenum():
    """Function that allows the user to enter a number."""
    while True:
        try:
            num = int(raw_input("  >*Enter a number: "))
            print ""
            print "Fibonacci in position", str(num), ":"
            print fib(num)
            new()
            break
        except ValueError:
            print "   Please enter a valid number!"

def new():
    """It allows entering a new number."""
    question = raw_input("Do you want to type another number? y/n ")
    questlow = question.lower()
    if questlow == "y" or questlow == "yes":
        typenum()
    elif questlow == "n" or questlow == "not":
        os.system("exit")
    else:
        print "Type 'y' or 'n'"
        new()

print ""
print "                 ----> *Fibonacci number* <----"
print ""
print "/*Enter a number, and the fibonacci number in the given position is displayed."
print ""
typenum()
