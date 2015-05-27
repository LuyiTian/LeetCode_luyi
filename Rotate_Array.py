class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        '''
        A little important thing to be cautious:

        nums[:] = nums[n-k:] + nums[:n-k] 
        can't be written as:

        nums = nums[n-k:] + nums[:n-k]
        on the OJ.

        The previous one can truly change the value of old nums,
        but the following one just changes its reference to a new 
        nums not the value of old nums.
        '''
        if k==0:
            return
        if k>len(nums):
            k = k%len(nums)
        if len(nums)==1:
            return
        a = nums[-k:]
        if not isinstance(a,list):
            a = [a]
        b = nums[:len(nums)-k]
        if not isinstance(b,list):
            b = [b]
        nums[:] = a+b


if __name__ == '__main__':
    A = Solution()
    A.rotate([1,2],1)