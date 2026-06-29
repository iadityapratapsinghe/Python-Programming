# To create a function that counts the occurence of vowels, consonants and other and retuen them as a key value pair in dictionary [ Strings ]:

def rusti(stro):
    v=0
    c=0
    t=0

    if type(stro)!=str:
        print("Invalid input")

    for i in stro:
        if i.isalpha():
            if i in "aeiouAEIOU":
                v=v+1
            else:
                c=c+1
        else:
            t=t+1

    print({
        "vowels":v,
        "consonants":c,
        "others":t
    })



stro="Hi 5!"

rusti(stro)