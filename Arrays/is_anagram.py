###################################Problem:###################################
"""
Given an integer array nums, return true if any value appears more than once in the array, 
    otherwise return false.
"""
###################################Solution:###################################
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if letters[i]:
                return False

        return True
###################################Approach:###################################

""" Solution:
The problem can be solved using a array as a hashmap and mapping every letter to an index between 0 - 26.
"""
#############################Time/Space Complexity:#############################

"""
 time complexity: O(N) - N == M if we make it past intial check. therfore worst case is alway O(N)
 space complexity: O(1) - array will always be of size 26
"""

#############################Misc Notes:#############################
""" Remember, things like checking if size is the same is alway an easy check.
"""