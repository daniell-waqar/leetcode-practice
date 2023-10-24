
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        i = 0
        while(i<j):

            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            j = j -1
            i = i+1
