# Factorial of a number : 

fact=1
n=int(input("Enter a number : "))
for  i in range(n,1,-1):
    fact=fact*i
print("Factorial is : ",fact)
