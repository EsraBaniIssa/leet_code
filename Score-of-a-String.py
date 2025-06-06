class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            diff = ord(s[i-1]) - ord(s[i])
            score = score + (diff if diff >= 0 else -diff)
        return score 