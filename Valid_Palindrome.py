class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        import string
        import math
        exclude = set(string.punctuation)
        s = ''.join(ch for ch in s if ch not in exclude)
        s = s.replace(' ', '')
        s = s.lower()
        if (not s) or (len(s) == 1):
            return True
        else:
            if s[:int(math.floor(len(s)/2.))] == s[int(math.ceil(len(s)/2.)):][::-1]:
                return True
        return False


if __name__ == '__main__':
    A = Solution()
    print A.isPalindrome('a ba')
