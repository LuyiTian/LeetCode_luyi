class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        '''
        I know it is not the required answer
        '''
        if not nums:
            return None
        nums = [-9999999999999999]+nums+[-9999999999999999]
        res = [nums[i-1]<nums[i]>nums[i+1] for i in range(1,len(nums)-1)]
        return res.index(True)-1

