from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixStr = ""

        for i in zip(*strs):
            if len(set(i)) == 1:
                prefixStr += i[0]
            else:
                break

        return prefixStr


x = Solution()
print(x.longestCommonPrefix(["flower", "flow", "flight"]))
