#To find compound interest

import math
P = int(input("Enter the principle amount:"))
R = float(input("Enter the rate percent:"))
T = int(input("Enter the time period:"))
A = P*(pow((1+R/100),T))
CI = A-P
print("The Amount is : ",A)
print("The Compound Intrest is : ",CI)
