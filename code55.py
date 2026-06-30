# To remove multiple spaces to a single space in a sentence [ Strings ]:

def removo(stro):
    result=""
    prev=""

    for i in stro:
        if i==" " and prev==" ":
            continue
        result=result+i
        prev=i
    print(result)
    



stro="Python    is fun"

removo(stro)