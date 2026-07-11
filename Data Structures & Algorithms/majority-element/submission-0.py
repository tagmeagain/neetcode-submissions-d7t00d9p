class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct.keys():
                dct[nums[i]]+=1
                if dct[nums[i]] > len(nums)//2:
                    return nums[i]
            else:
                dct[nums[i]]=1
        return nums[i]