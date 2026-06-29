# To remove trailing vowels from backwards [ Arrays ]:

def removo(stro):

    for i in stro[::-1]:
        if i in "aeiouAEIOU":
            stro=stro[:-1]
            
        else:
            break
    print(stro)
        
    
        
    
stro="idea"

removo(stro)