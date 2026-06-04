class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)

        while left<=right:
            mid=math.floor(left+right)//2
            print("Mid",mid)
            if target==nums[mid]:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1