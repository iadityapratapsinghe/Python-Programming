# To find the index of a targeted number in an sorted array :

def find(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
         print(i)


nums=[1,2,9,0,1]
target=9

find(nums,target)

