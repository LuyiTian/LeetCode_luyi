"""
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        '''
        thanks to Python we have shortcut. but not what I want
        '''
        res = nums1+nums2
        res.sort()
        if len(res) % 2 == 0:
            return 0.5*(res[-1+len(res)/2]+res[len(res)/2])
        return res[len(res)/2]
"""


#now try the hard way
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        print nums1, nums2
        def get_medi(arr):
            if len(arr) % 2 == 0:
                return 0.5*(arr[-1+len(arr)/2]+arr[len(arr)/2])
            return arr[len(arr)/2]
        if not nums1:
            return get_medi(nums2)
        elif not nums2:
            return get_medi(nums1)
        elif len(nums1) <= 2 or len(nums2) <= 2:
            res = nums1+nums2  # shouldn't be done this way, I am just lazy
            res.sort()
            return get_medi(res)
        else:
            if get_medi(nums1) > get_medi(nums2):
                if len(nums1) >= len(nums2):
                    if len(nums2) % 2 == 0:
                        return self.findMedianSortedArrays(nums1[:1-(len(nums2)/2)], nums2[-1+len(nums2)/2:])
                    else:
                        return self.findMedianSortedArrays(nums1[:-(len(nums2)/2)], nums2[len(nums2)/2:])
                else:
                    if len(nums1) % 2 == 0:
                        return self.findMedianSortedArrays(nums1[:1-(len(nums1)/2)], nums2[-1+len(nums1)/2:])
                    else:
                        return self.findMedianSortedArrays(nums1[:-(len(nums1)/2)], nums2[len(nums1)/2:])
            elif get_medi(nums2) > get_medi(nums1):
                if len(nums2) >= len(nums1):
                    if len(nums1) % 2 == 0:
                        return self.findMedianSortedArrays(nums2[:1-(len(nums1)/2)], nums1[-1+len(nums1)/2:])
                    else:
                        return self.findMedianSortedArrays(nums2[:-(len(nums1)/2)], nums1[len(nums1)/2:])
                else:
                    if len(nums2) % 2 == 0:
                        return self.findMedianSortedArrays(nums2[:1-(len(nums2)/2)], nums1[-1+len(nums2)/2:])
                    else:
                        return self.findMedianSortedArrays(nums2[:-(len(nums2)/2)], nums1[len(nums2)/2:])
            else:
                return get_medi(nums1)


if __name__ == '__main__':
    A = Solution()
    print A.findMedianSortedArrays([1,2,3], [4,5,6,7])
    print A.findMedianSortedArrays([1,2,3], [4,5,6])
    print A.findMedianSortedArrays([1,5,6], [2,3,4,7])
    print A.findMedianSortedArrays([1,2,3], [4,5,6,7,8])
    print A.findMedianSortedArrays([1,2,6], [3,4,5])
    print A.findMedianSortedArrays([1,2,6,7], [3,4,5,8])

