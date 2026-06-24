# Print n to 1 by recurssion :


n=int(input("Enter a number : "))

def recci(n):
    if(n==0):
        return
    print(n)
    recci(n-1)

recci(n)