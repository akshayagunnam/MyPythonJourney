#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            index = nums.index(target)
            return index
        else:
            nums.append(target)
            nums.sort()
            index = nums.index(target)
            return index
