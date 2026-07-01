class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        nums = list(set(nums))
        length_new = len(nums)
        if length != length_new:
            return True
        else:
            return False
        