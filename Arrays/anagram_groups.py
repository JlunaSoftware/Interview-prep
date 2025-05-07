###################################Problem:###################################
"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""
###################################Solution:###################################
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # {(tuple of 26 ltrs) : List[strs]}
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            anagrams[tuple(letters)].append(s)
        
        return anagrams.values()
###################################Approach:###################################

""" Solution:
The problem can be solved using a Dictionary where the key is a tuple of the count of letter counts in each word 
    and value is list of all strings the correlate to that tuple

    anagrams = {(0,1,2,3..26) : ["cat", "atc"], ...}
"""

#############################Time/Space Complexity:#############################

"""
Solution 1:
 time complexity: O(N * M)
 space complexity: O(N)

 where N is number strings in strs and M is length of longest strings
"""

#############################Misc Notes:#############################
"""
defaultdicts simplifies the code and makes answer easier to derive
"""