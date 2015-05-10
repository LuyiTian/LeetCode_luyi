class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if max(nums) == 0:
            return '0'

        def cmp_fun(x, y):
            if int(str(x)+str(y)) > int(str(y)+str(x)):
                return 1
            elif int(str(x)+str(y)) == int(str(y)+str(x)):
                return 0
            else:
                return -1
        nums.sort(cmp=cmp_fun)
        return ''.join([str(it) for it in nums[::-1]])

if __name__ == '__main__':
    A = Solution()
    print A.largestNumber([2,1])