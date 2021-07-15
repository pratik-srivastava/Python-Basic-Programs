#To check wether given number is Armstrong number or not

import math
num = int(input("Enter the number:"))
n = num
s=0
while(num!=0):
    a=num%10
    s=s+pow(a,3)
    num=num//10

if n == s:
    print("Armstrong Number")

else:
    print("Not a Armstrong number")
