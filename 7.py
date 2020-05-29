class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        flag = 1
        if x < 0:
            x *= -1
            flag = -flag
        while x != 0:
            sum = sum * 10 + x % 10
            x //= 10
        return sum * flag if -2 ** 31 < sum * flag < 2 ** 31 else 0


x = Solution()
print(x.reverse(123456))
