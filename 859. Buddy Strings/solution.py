class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Check if the lengths of the strings are the same
        if len(s) != len(goal):
            return False

        # If the strings are equal, check if there are repeated characters
        if s == goal and len(set(s)) < len(s):
            return True

        # Find the indices where the characters are different
        diff_indices = [i for i in range(len(s)) if s[i] != goal[i]]

        # Check if there are exactly two differences and swapping makes the strings equal
        return len(diff_indices) == 2 and s[diff_indices[0]] == goal[diff_indices[1]] and s[diff_indices[1]] == goal[diff_indices[0]]
