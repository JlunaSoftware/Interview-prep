###################################Problem:###################################
"""
Given an integer array nums, return true if any value appears more than once in the array, 
    otherwise return false.
"""
###################################Solution:###################################
""" Solution 1:
The problem can be solved using a set to keep track of the numbers we have seen so far.
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

"""Solution 2:
If length of set of unique numbers in list is less than original list length
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
###################################Approach:###################################

""" Solution 1:
The problem can be solved using a set to keep track of the numbers we have seen so far.
    If a duplicate appears immediately return True
"""

""" Solution 2:
If length of set of unique numbers in list is less than original list length
"""

#############################Time/Space Complexity:#############################

"""
Solution 1:
 time complexity: O(N)
 space complexity: O(N)

Solution 2: 
 time complexity: O(N)
 space complexity: O(N)
"""

#############################Misc Notes:#############################
"""
Although Solution 2 is better, solution 1 is easily obtainable and contains same time and space
complexity
"""