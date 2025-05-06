###################################Problem:###################################
"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first. 
"""
###################################Solution:###################################
""" Solution 1:
The problem can be solved using a dictionary with the nums[i] as the key and idx as the value.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # {num : idx}

        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                return [seen[target - nums[i]], i]
            seen[nums[i]] = i

###################################Approach:###################################

""" Solution:
The problem can be solved using a Dictionary to keep track of previously seen values.
"""

#############################Time/Space Complexity:#############################

"""
Solution:
 time complexity: O(N)
 space complexity: O(N)
"""

#############################Misc Notes:#############################
"""
N/A
"""