class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not (len(nums) == len(set(nums))):
            return True
        return False