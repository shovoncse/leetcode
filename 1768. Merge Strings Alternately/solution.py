class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        output = list(word1)
        pointer  = 1
        for ch in word2:
            output.insert(pointer, ch)
            pointer += 2

        return ''.join(output)