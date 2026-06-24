# To create a function that prints the dictionary having value greater than the target value [ Dictionary ]:


def filtero(dictn1,threshold):

    dictn2={}

    if type(dictn1)!=dict:
     print(" Invalid ")


    for key in dictn1:
       if dictn1[key]>threshold:
          dictn2[key]=dictn1[key]
    print(dictn2)


dictn1={"laptop":1200,"mouse":25,"monitor":200}
threshold=100

filtero(dictn1,threshold)