# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if str(x) == str(x)[::-1]:
#             return True
#         return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the number is negative, as negative numbers cannot be palindromes
        if x < 0:
            return False
        
        # Initialize variables for reversing the number and storing the original number
        reverse = 0
        temp = x
        
        # Reverse the digits of the number
        while temp != 0:
            reverse = reverse * 10 + temp % 10  # Extract the last digit and add it to the reversed number
            temp = temp // 10  # Remove the last digit from the original number
        
        # Check if the reversed number is equal to the original number
        return reverse == x