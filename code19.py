# To enter marks of n subjects and store them in a dictionary as key value pairs : 

d={}
n=int(input("Enter number of subject marks you want to enter : "))
for i in range(1,n+1):
    b=input("Enter subject : ")
    a=int(input("Enter marks : "))
    d[b]=a

print(d)



