# Function to calculate average of n numbers :

def average():
    n=int(input("Enter quantity of number : "))
    s=0
    for i in range(1,n+1):
        a=int(input("Enter a number : "))
      
        s=s+a
        t=s/n
    print("Average will be : ",t)

average()





