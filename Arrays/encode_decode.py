###################################Problem:###################################
"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
"""
###################################Solution:###################################
""" Solution:
The problem can be solved by prefixing each string with its length and an ending symbol
"""
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += f"{len(string)}#" + string
        return res

    def decode(self, s: str) -> List[str]:
            res = []
            i = 0
            while i < len(s):
                word_len = ""
                while s[i] != "#":
                    word_len += s[i]
                    i += 1
                i += 1
                res.append(s[i : i + int(word_len)])
                i += int(word_len)

            return res

###################################Approach:###################################

""" Solution:
Encode: create a single output string made up of all strings in strs list, each string is prefixed
    with its length and an delimiter for length ("#")

Decode: Since we are only given valid solutions, find "#" use chars left of it get length of string.
continue until all strings have been extracted
"""

#############################Time/Space Complexity:#############################

"""
Encode:
 time complexity: O(M)
 space complexity: O(N + M)

Decode:
 time complexity: O(M)
 space complexity: O(N + M)

 Where M is sum length of all strings 
"""

#############################Misc Notes:#############################
"""
Trick is to realize that'll you have to know length and will have to extract length from rest of string.
"""