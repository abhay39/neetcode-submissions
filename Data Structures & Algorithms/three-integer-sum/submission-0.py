class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
    
        result = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum == 0:  # Found a triplet that sums to zero
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates of second and third elements
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total_sum < 0:  # Move the left pointer to get a larger sum
                    left += 1
                
                else:  # Move the right pointer to get a smaller sum
                    right -= 1
        
        return result