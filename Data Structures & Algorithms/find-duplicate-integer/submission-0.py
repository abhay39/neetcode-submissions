class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        
        for key, values in dict.items():
            if values>=2:
                return key
        return 0