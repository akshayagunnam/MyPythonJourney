"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        for i in range (count):
            nums.remove(0)
        for i in range (count):
            nums.append(0)
        return nums
