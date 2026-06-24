# To get max score from dictionary [ Dictionary ]:

def maxino(students):
 max=0
 topper=" " 

 for name in students:
    if students[name]>max:
        max=students[name]
        topper=name
 print(topper)

students={"aditya":50 , "Praveen":90 , "reenu":70}

maxino(students)