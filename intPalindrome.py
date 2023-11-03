class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        reverse = x_str[::-1]

        if x_str == reverse:
            return True
        else:
            return False
        