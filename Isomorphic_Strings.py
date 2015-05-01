class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        tmp_dict_s = {}
        tmp_dict_t = {}
        for i, j in zip(s, t):
            if i not in tmp_dict_s:
                tmp_dict_s[i] = j
            elif tmp_dict_s[i] != j:
                return False
            if j not in tmp_dict_t:
                tmp_dict_t[j] = i
            elif tmp_dict_t[j] != i:
                return False
        return True


if __name__ == '__main__':
    A = Solution()
    print A.isIsomorphic('ab', 'ca')
