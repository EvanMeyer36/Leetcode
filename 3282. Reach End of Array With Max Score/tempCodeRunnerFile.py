    def findMaximumScore(self, nums: list[int]) -> int:
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