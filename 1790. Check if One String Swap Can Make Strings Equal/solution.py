class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        if s1 == s2:
            return True
        
        diff_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]

        return len(diff_indices) == 2 and s1[diff_indices[0]] == s2[diff_indices[1]] and s1[diff_indices[1]] == s2[diff_indices[0]]