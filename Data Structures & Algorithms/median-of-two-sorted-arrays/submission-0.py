class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result=float(1)

        nums1.extend(nums2)
        print(nums1)
        sum_val=sum(nums1)
        print(sum_val)
        return sum_val/len(nums1)