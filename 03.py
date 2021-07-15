#To find factorial of a number

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)


n = int(input("Enter the number whose factorial is to be found: "))
fact = factorial(n)
print("Factorial of ",n," is :-",fact)
