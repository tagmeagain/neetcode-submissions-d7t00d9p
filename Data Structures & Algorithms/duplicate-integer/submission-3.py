class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct:
                return True
            dct[nums[i]] = 0
        return False
