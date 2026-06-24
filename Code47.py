# To create a function in which we have to sum up the values if their keys are same from di-dictionaries[ Dictionary ]:

def dambar(dictn1,dictn2):

    result={}
    
    for key in dictn1:

        if key in dictn2:
            dictn2[key]=dictn1[key]+dictn2[key]

        else:
            dictn2[key]=dictn1[key]

    print(dictn2)
       





dictn1={'apple':5,'eggs':12}

dictn2={'apple':10,'milk':2}

dambar(dictn1,dictn2)
