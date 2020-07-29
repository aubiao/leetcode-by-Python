from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)

        return len(nums)


x = Solution()
a = [1, 2, 3, 3, 2]
print(x.removeElement(a, 2))
print(a)
