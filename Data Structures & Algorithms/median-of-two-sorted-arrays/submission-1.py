from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m

        while left <= right:
            cut1 = (left + right) // 2
            cut2 = half - cut1

            Aleft = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            Aright = float('inf') if cut1 == m else nums1[cut1]

            Bleft = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            Bright = float('inf') if cut2 == n else nums2[cut2]

            if Aleft <= Bright and Bleft <= Aright:
                # Correct partition found
                if total % 2:
                    return max(Aleft, Bleft)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = cut1 - 1
            else:
                left = cut1 + 1