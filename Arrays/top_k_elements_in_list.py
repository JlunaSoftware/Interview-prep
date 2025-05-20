###################################Problem:###################################
"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""
###################################Solution:###################################
""" Solution 1:
The problem can be solved using a dictionary { val: cnt } and optimized heap
"""
from collections import Counter, defaultdict
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            # O(logK) optimization
            if len(heap) > k:
                heapq.heappop(heap)

        return [ heap[i][1] for i in range(len(heap))]

"""Solution 2:
The problem can be solved using bucket sort. Where buckets are 0...N, where N is number of items in nums list.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        counts = Counter(nums)
        bucket = defaultdict(list)
        for val, cnt in counts.items():
            bucket[cnt].append(val)

        res = []
        for i in range(N, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res
###################################Approach:###################################

""" Solution 1:
Uses Counter function to get dictionary of { val: cnt }. Uses Heap of size k to filter top k elements
"""

""" Solution 2:
Bucket Sort, Each bucket is 0..N where is N is max number of items, highest count possible.
"""

#############################Time/Space Complexity:#############################

"""
Solution 1:
 time complexity: O(NLogK)
 space complexity: O(N + K)

Solution 2: 
 time complexity: O(N)
 space complexity: O(N)
"""

#############################Misc Notes:#############################
"""
Bucket sort is the optimal solution. The trick is to realize that creating dictionary of list wher val is key and counts list is value.
Leads us to O(N) time & space complexity
"""