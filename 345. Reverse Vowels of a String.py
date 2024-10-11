"""
345. Reverse Vowels of a String

Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.


"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        items = list(s)
        left_pointer = 0
        right_pointer = len(items) - 1

        while left_pointer < right_pointer:
            left_true = items[left_pointer].lower() in ['a','e', 'i', 'o', 'u']
            right_true = items[right_pointer].lower() in ['a','e', 'i', 'o', 'u']

            if left_true:
                if right_true:
                    items[left_pointer], items[right_pointer] = items[right_pointer], items[left_pointer]
                    right_pointer -=1
                    left_pointer +=1
                else:
                    right_pointer -=1
            elif right_true:
                left_pointer +=1
            else:
                right_pointer -=1
                left_pointer +=1
        
        return ''.join(items)
