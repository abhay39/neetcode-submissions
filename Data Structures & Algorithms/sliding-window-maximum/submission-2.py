from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # stores indexes

        for right in range(len(nums)):

            # 1. Remove indexes outside the current window
            while dq and dq[0] < right - k + 1:
                dq.popleft()

            # 2. Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # 3. Add current index
            dq.append(right)

            # 4. Once window reaches size k, front is maximum
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result