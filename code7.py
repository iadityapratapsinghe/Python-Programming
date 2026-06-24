# PRogram to find the occurence of $ in a string

a=input("Enter your text : ")
c=0
for i in a:
    if (i=="$"):
        c=c+1
print(c)
