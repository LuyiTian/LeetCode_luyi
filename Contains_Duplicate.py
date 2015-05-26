class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(set(nums))<len(nums):
            return True
        else:
            return False
        