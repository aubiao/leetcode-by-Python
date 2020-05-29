class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        sum = 0
        while num != 0:
            sum = sum * 10 + num % 10
            num //= 10
        return sum == x


x = Solution()
print(x.isPalindrome(12321))
