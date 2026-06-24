# To print odd when number is odd and even when number is even : 

a=int(input("Enter a number : "))

def check(a):
    if a%2==0:
        print("Even number")
    else:
        print("Odd number")

check(a)