class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dct = ""
        for i in range(len(strs[0])):
            for s in strs:
                print(s)
                if strs[0][:i+1] in s[:i+1]:
                    continue
                else:
                    return dct
            dct+= strs[0][i]
        return dct
