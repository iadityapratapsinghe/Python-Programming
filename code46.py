# To create a python function in which we have to swap keys and values & if multiple keys map to same values , store key in a list :


def swap_values(dictn):

    result={}

    for key in dictn:

        value=dictn[key]
        
        if value not in result:
            result[value]=[key]
        else:
            result[value].append(key)

    print(result)





dictn = {'a':1,'b':2,'c':1}

swap_values(dictn)