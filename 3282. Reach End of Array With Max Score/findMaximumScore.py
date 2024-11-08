import sys

def findMaximumScore(nums) -> int:
    sum = 0
    i = 0
    j = i+1
    for i in range(len(nums)-1):
        if nums[i]< nums[j]:
            sum +=(j -i) * nums[i]
        if j == len(nums)-1:
            sum +=(j -i) * nums[i]
        else:
            j+=1
    return sum

nums = [1,3,1,5]
print(findMaximumScore(nums))

nums = [4,3,1,3,2]
print(findMaximumScore(nums))