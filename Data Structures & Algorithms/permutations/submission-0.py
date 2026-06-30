from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm_tuples = permutations(nums)
        
        # 2. Convert the iterator into a list of lists (to match the required type List[List[int]])
        # We use list(p) inside the comprehension to convert each tuple 'p' into a list.
        result = [list(p) for p in perm_tuples]

        # 3. Return the final list of lists
        return result