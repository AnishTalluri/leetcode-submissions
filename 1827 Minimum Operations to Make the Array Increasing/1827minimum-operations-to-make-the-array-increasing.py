class Solution:
    def minOperations(self, nums: List[int]) -> int:
        increments = 0
        diff = 0
        min_increments = 0
        for i in range(0, len(nums)-1):
            if nums[i] >= nums[i+1]:
                diff = nums[i] - nums[i+1]
                min_increments = diff + 1
                nums[i+1] += min_increments
                increments += min_increments
        return increments
