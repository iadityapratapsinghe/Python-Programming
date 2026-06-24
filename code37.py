# Sum of first n natural number through recurssion :

n = int(input("Enter a number : "))

def add(n):
    
    if(n==1 or n==0):
        return 1 
    else:
        return n + add(n-1)
    
print(add(n))