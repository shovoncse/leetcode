class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {} # mapping charCount to list of Anagrams
        res = defaultdict(list)
        
        for s in strs:
          count = [0] * 26 # a ... z
          
          for c in s:
            count[ord(c) - ord("a")] += 1
            
          # res[count].append(s) # List can't be index
          res[tuple(count)].append(s)
        
        return res.values()
      
# optimal O(m*n) solution - m is the number of strings given, n is the length of string