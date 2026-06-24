# To print the indices of a list whose sum matches with the target value [ Array ]: 
target=9
nums=[2,7,11,15]
   
def twosum(nums ,target):

 for i in range(len(nums)):
   for j in range(i+1,len(nums)):
      if nums[i]+nums[j]==target:
        print([i,j])
   

twosum(nums,target)

