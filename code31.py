# To print elemsnta of list :

def dumbo():
    l=[]
    n=int(input("Enter quantity of elements : "))
    for i in range(1,n+1):
        a=input("Enter an element : ")
        l.append(a)
    for n in l:
     print(n)

dumbo()