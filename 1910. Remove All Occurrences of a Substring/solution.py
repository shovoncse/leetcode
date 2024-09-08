class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        final_str = s
        part_len = len(part)
        while True:
            
            index_now = self.findIndex(final_str, part)
            if index_now == -1:
                break
            
            final_str = self.delete_substring(final_str, index_now, index_now + part_len)
        
        return final_str


    def findIndex(self, str_, sub_str):
        index = str_.find(sub_str)
        return index
    
    def delete_substring(self, s, start, end):
        return s[:start] + s[end:]