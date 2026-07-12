class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        count = 0
        prefix = 0
        for arr in nums:
            prefix+=arr
            if prefix-k in dct:
                count+=dct[prefix - k]
            dct[prefix] = dct.get(prefix,0)+1
        return count