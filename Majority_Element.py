class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        for i in list(set(nums)):
            if nums.count(i)> len(nums)/2.:
                return i


if __name__ == '__main__':
    A = Solution()
    A.majorityElement([3,2,7,1,9])