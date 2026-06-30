#sp

from math import sqrt

try:
    num =float(input("Enter Number: "))
    print("num = ",num)

    if num >=0:
        print("sqrt =",round(sqrt(num),2))
    else:
        print("Please enter positive number only")

except ValueError:
    print("Please enter Number")