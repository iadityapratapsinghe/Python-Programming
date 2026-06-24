# Search for a number in tuple :

t=(1,4,9,16,25)
a=int(input("Enter your number you want to search : "))
for i in t :
    if(i==a):
        print("Number found")
        break
else:
    print("Number not found") 