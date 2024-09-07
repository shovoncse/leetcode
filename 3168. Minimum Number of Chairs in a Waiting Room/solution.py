class Solution:
    def minimumChairs(self, s: str) -> int:
        self.max = 0
        now = 0
        for i in s:
            if i == "E":
                now += 1
            if i == "L":
                now -= 1

            self.checkMax(now)

        return self.max

    def checkMax(self,val):
        if val > self.max:
            self.max = val