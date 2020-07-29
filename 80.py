from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cnt = 1
        i = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                cnt += 1
                if cnt <= 2:
                    i += 1
                    nums[i] = nums[j]
            else:
                i += 1
                nums[i] = nums[j]
                cnt = 1
        return i + 1


x = Solution()
a = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(x.removeDuplicates(a))
