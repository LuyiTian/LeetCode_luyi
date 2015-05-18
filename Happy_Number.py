class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        res_dict = {}
        res_dict[n] = sum([int(it)*int(it) for it in str(n)])
        if res_dict[n] == 1:
            return True
        tmp_val = res_dict[n]
        iter_n = 0
        while iter_n < 10000:
            if tmp_val in res_dict:
                return False
            else:
                tmp_result = sum([int(it)*int(it) for it in str(tmp_val)])
                if tmp_result == 1:
                    return True
                else:
                    res_dict[tmp_val] = tmp_result
                    tmp_val = tmp_result
            iter_n += 1
