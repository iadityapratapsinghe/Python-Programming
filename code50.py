# To create a function which gives unique words from a string [ Strings ]:


def tampo(stro):
  try:
    l=[]
    
    stro=stro.replace("."," ")
    words=stro.split() 

    for i in words:
      if i not in l:
         l.append(i)
    print(l)

  except:
    print("Invalid Input")






stro="Data Science is great.Science is fun"


tampo(stro)