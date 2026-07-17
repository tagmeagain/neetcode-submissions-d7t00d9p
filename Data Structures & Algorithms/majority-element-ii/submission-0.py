class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)//3
        dct = {}
        ls = []
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] not in dct:
                dct[nums[i]]=1
            else:
                dct[nums[i]]+=1
            print(dct[nums[i]])
            if dct[nums[i]]>size and nums[i] not in ls:
                ls.append(nums[i])
        return ls