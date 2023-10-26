
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example:

# Input: digits = [1,2,3]
# Output: [1,2,4]


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits  
            else:
                digits[i] = 0
        
        if digits[0] == 0:
            result = [0] * (n + 1)
            result[0] = 1
            return result
        else:
            return digits  # Return digits if no carry occurs
