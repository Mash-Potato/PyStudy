class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lt = 0
        rt = len(s)-1
        while lt < rt:
            s[lt], s[rt] = s[rt], s[lt]
            lt += 1
            rt -= 1

