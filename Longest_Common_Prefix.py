class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            prefix_list = []
            for i in range(min([len(t) for t in strs])):
                col_st = [st[i] for st in strs]
                prefix_list.append([cr if col_st.count(cr) == len(strs) else 1 for cr in col_st])
            prefix_list = zip(*prefix_list)
            tmp_max = -1
            lst_pre = ""
            for st in prefix_list:
                if 1 not in st:
                    if len(st)-1>tmp_max:
                        tmp_max = len(st)-1
                        lst_pre = ''.join(st)
                elif st.index(1) > tmp_max:
                    tmp_max = st.index(1)
                    lst_pre = ''.join(st[:st.index(1)])
            return lst_pre


if __name__ == '__main__':
    A = Solution()
    print A.longestCommonPrefix(['a','a','b'])
