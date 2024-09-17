class Solution(object):
    def findKOr(self, nums, k):
        bnums = []
        m = len(bin(max(nums))[2:])
        for num in nums:
            b = bin(num)[2:]
            if len(b) < m:
                b = "0"*(m - len(b)) + b
            bs = []
            for s in b:
                bs.append(s)
            bnums.append(bs)
        newBit = ""
        sum = 0
        for col in range(m):
            for row in range(len(bnums)):
                if bnums[row][col] == "1":
                    sum+=1
            if sum >= k:
                newBit += "1"
            else:
                newBit += "0"
            sum = 0 
        return int(newBit, 2)