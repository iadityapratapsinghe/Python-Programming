# To find greatest of three numbers entered by user : 

a=int(input("Enter a number a : "))
b=int(input("Enter a number b : "))
c=int(input("Enter a number c : "))
if(a>b and a>c):
    print(" a is the greatest ")
elif(b>c):
    print(" b is the greatest ")
else:
    print(" c is the greatest ")