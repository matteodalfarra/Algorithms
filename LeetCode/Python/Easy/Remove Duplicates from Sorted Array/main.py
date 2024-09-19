class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 1
        index = 1
        while i < n:
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
            i+=1
        return index