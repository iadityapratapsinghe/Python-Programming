# Factorial of n (n is the parameter) :

n=int(input("Enter your number : "))
def typo(n):
    fact=1
    for i in range(n,1,-1):
        fact=fact*i
    print("Factorial is : ",fact)


typo(n)