# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.
import numpy as np


x = input("Enter number x: ")
y = input("Enter number y: ")
pow = int(x)**int(y)
log = np.log2(int(x))
print("x**y = " + str(pow))
print("log(x) = " + str(log))