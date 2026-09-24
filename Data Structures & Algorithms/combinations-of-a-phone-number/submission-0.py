class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
            
        nums = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # Start with an empty string in the result list
        result = [""]
        
        for digit in digits:
            temp_list = []
            # For each existing combination, append the new letters
            for combo in result:
                for letter in nums[digit]:
                    temp_list.append(combo + letter)
            # Update result with the new longer combinations
            result = temp_list
            
        return result