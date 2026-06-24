# Sum of squared evn numbers  [ loops ]: 

def trit(nums):
    m=0

    
    for i in nums:

        if type(i)==str:
         print("Invalid input")
         return

        if i%2==0:
            k=i*i
            m=m+k
    print(m)
        

nums=[1,2,3,4,"a"]

trit(nums)