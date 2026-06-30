#POP 

def show(num):
    print("num = ",num)

def sqrt(num):
    if num>=0:
        ans = num**0.5
        print("sqrt =", round(ans,2))
    else:
        print("Please enter positive number only")

try:
    num = float(input("Enter Number: "))
    show(num)
    sqrt(num)
    
except ValueError:
    print("Please enter Number only")