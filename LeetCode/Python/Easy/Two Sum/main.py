class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums)-1):
            for v in range(n, len(nums)):
                if n != v:
                    if nums[v] + nums[n] == target:
                        return [n, v]