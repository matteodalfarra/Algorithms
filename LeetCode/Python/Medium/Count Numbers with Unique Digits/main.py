class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        tot = 1
        for i in range(1, n+1):
            p = 9
            for j in range(2, i + 1):
                p *= 10-j+1
            tot += p
        return tot