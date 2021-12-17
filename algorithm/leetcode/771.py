class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(char in jewels for char in stones)