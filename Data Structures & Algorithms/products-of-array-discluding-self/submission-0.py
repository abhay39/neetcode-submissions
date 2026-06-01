class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # calculate running product from left
        left_product = 1
        for i in range(n):
            output[i] *= left_product
            left_product *= nums[i]
        
        # calculate running product from right
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output