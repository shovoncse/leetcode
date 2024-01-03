class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = []
        # Count the number of "beams" in each string
        for i in range(len(bank)):
            beams = bank[i].count('1')
            if beams > 0:
                arr.append(beams)
                
        # *** NOTE: beams_count = [s.count('1') for s in bank if '1' in s] is a more efficient way to do this ***

        # If there are less than 2 "beams," return 0
        if len(arr) < 2:
            return 0

        # Calculate the sum using a list comprehension
        sum_result = sum(arr[i] * arr[i + 1] for i in range(len(arr) - 1))

        return sum_result