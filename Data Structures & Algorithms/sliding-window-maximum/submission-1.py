class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        n=len(nums)

        for i in range(n-k+1):
            curr=i
            temp=[]
            for j in range(k):
                temp.append(nums[i+j])
            maxi=max(temp)
            result.append(maxi)
        return result
            