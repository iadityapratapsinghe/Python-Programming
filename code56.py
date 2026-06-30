# To insert a word in a string at specific index [ Strings ]:

def entro(stro,word,n):

    result=""

    if type(stro)!=str or type(word)!=str or type(n)!=int:
        print("Invalid input")
    if n<0 or n>len(stro):
        print("Index out of range")

    for i in range(len(stro)):
        if i==n:
            result=result+word

        result=result+stro[i]

    if n==len(stro):
        result=result + word

    return result


print(entro("Python is great","Programming ",10))