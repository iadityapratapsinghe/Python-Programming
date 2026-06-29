# To create a function that counts vowels and consonants in a string [ Strings ]:


def counti(stro):
 v=0
 c=0

 for i in stro:
  if i.isalpha():
   if i in "aeiouAEIOU":
     v=v+1
   else:
      c=c+1
 print("vowel count",v)
 print("Consonant count",c)





stro="pyt hon3.11"

counti(stro)
