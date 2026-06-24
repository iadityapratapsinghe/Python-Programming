# Function to print the length of a list : 


def tonka():
    l=[]
    n=int(input("Enter strength of the elements : "))
    for i in range(1,n+1):
        a=input("Enter the element : ")
        l.append(a)
    print("The length of the list is : ",len(l))

tonka()