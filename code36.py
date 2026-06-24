# Factorial through recurssion : 


n= int(input("Enter a number : "))
def fick(n):
    if(n==0 or n==1):
        return 1 
    else:
        return n * fick(n-1)


print(fick(n))