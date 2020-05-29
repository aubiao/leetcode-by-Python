class Solution:
    def romanToInt(self, s: str) -> int:
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        slen = len(s)

        if slen == 1:
            return m[s]

        a = m[s[0]]

        for i in range(1, slen):
            if m[s[i]] > m[s[i-1]]:
                a -= m[s[i-1]] * 2 - m[s[i]]
            else:
                a += m[s[i]]
        return a


x = Solution()
print(x.romanToInt('IV'))
