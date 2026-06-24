# To move zeroes in the last of the list [Array]: 

def movezeroes(nums):
 nonzero=[]
 for i in nums:
  if i!=0:
   nonzero.append(i)

 zerocount=len(nums)-len(nonzero)
 for k in range(zerocount):
  nonzero.append(0)

 print(nonzero)
  

nums=[11,0,2,9,0,7,0]

movezeroes(nums)

