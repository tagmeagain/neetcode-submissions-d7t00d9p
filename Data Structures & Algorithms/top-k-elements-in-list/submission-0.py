class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct:
                dct[nums[i]]+=1
            else:
                dct[nums[i]]=1
        return sorted(dct, key = lambda x: dct[x],reverse=True)[:k]