class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        listt = []

        listt.extend(nums1)
        listt.extend(nums2)

        listt.sort()

        n = len(listt)

        if n % 2 == 0:
            left = n // 2 - 1
            right = n // 2

            return (listt[left] + listt[right]) / 2

        else:
            mid = n // 2

            return listt[mid]