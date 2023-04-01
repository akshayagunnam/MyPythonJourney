#xGiven an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
