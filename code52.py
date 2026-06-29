# To print the longest word in a sentence [ Strings ]:


def longo(stro):

    t=0
    longest=""

    if type(stro)!=str:
        print("Invalid input")



    words=stro.split()

    if len(words)==0:
       return""

    for i in words:
      if len(i)>t:
         t=len(i)
         longest=i

    print(longest)


stro="The quick brown fox jump over the lazy dog"

longo(stro)