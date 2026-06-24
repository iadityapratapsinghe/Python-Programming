# To print all elements of a list through recurrsion :



def elem(l,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    elem(list,idx+1)

list=["mango","apple","guava","strawberry"]

elem(list)
    