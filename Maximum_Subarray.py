class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        max_ending_here = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far