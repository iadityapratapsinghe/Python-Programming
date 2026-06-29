# To print first non-repeating character [ Arrays ]:

def nonro(stro):


    for i in stro:
        if stro.count(i)==1:
         print(i)
    return -1

stro="racecar"

nonro(stro)