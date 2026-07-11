class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        ls = []
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in dct.keys():
                dct["".join(sorted(strs[i]))].append(strs[i])
            else:
                dct["".join(sorted(strs[i]))] = [strs[i]]
        return list(dct.values())        