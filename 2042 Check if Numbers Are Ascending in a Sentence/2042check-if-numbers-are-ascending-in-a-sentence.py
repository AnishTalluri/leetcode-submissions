class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # Split string into an array
        # Parse array
        # If array has numbers, check sequential numbers against each other repeatedly check it,
        # if it fails then return false
        check_num = -1
        sentence = s.split(" ")
        nums = []

        for digit in sentence:
            if digit.isdigit():
                nums.append(int(digit))
        
        check_num = nums[0]
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i+1]:
                check_nums = nums[i+1]
            else:
                return False
        return True
