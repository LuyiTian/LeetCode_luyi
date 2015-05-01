class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        rep_dict = {}
        for i in range(len(s)-9):
            if s[i:i+10] in rep_dict:
                rep_dict[s[i:i+10]] += 1
            else:
                rep_dict[s[i:i+10]] = 1
        return [k for k, v in rep_dict.items() if v > 1]


if __name__ == '__main__':
    A = Solution()
    print A.findRepeatedDnaSequences("AAAAAAAAAAA")
