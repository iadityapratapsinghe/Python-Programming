# To remove duplicate numbers from a sorted array without creating a new array :


def removeduplicate(nums):
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[k-1]:
            nums[k]=nums[i]
            k=k+1
    print(k)
    print(nums[:k])



nums=[0,0,1,1,1,2,2,3,3,4]

removeduplicate(nums)