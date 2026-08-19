class Solution:
    def hasDuplicate(self,nums):
        s = set()
        for i in nums:
            s.add(i)
        return len(s) != len(nums)