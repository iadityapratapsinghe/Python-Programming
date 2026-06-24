# License system :

a=int(input("Enter your age : "))
if(a>=18):
    print("Eligible for license")
elif(a==16 or 17 ):
    print("Eligible for minor's license")
elif(a>80):
     print("License expired")
else:
    print("Under eligibility")

