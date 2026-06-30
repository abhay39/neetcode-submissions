from itertools import permutations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]] 

        for num in nums:
            current_size = len(result) 
            for i in range(current_size):
                subset_to_copy = list(result[i]) 
                new_subset = subset_to_copy + [num] 
                result.append(new_subset)
        
        return result