class Solution:
    def isScramble(self, s1: str, s2: str, memo=None) -> bool:
        if memo is None:
            memo = {}
        
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        
        if len(s1) <= 1 and s1 != s2:
            return False
        
        if s1 == s2:
            return True
        
        if (s1, s2) in memo:
            return memo[s1, s2]
        
        n = len(s1)
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i], memo) and self.isScramble(s1[i:], s2[i:], memo)) \
            or (self.isScramble(s1[:i], s2[-i:], memo) and self.isScramble(s1[i:], s2[:-i], memo)):
                memo[s1, s2] = True
                return True
        
        memo[s1, s2] = False
        return False
