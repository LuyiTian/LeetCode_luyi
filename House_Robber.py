class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        '''
        f(j) indicates the robber has made a dicison for 
        jth house for the max money, the recursion can
        be f(j) = max(f(j-1), f(j-2)+nums[j])
        '''
        x0 = 0; x1 = 0; x2 = 0
        for i in range(len(nums)):
            x2 = max(x0+nums[i],x1)
            x0 = x1
            x1 = x2
        return x2
}



