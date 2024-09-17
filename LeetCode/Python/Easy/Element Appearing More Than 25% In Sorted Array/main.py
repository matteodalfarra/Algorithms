class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        minElement = n * 25 / 100

        elements = dict()

        for v in arr:
            if v in elements.keys():
                elements[v] += 1
            else:
                elements[v] = 1

        num = 0
        rep = 0
        for v in elements.keys():
            if elements[v] > rep:
                rep = elements[v]
                num = v

        if rep > minElement:
            return num