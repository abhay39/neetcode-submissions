class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[]
        for i in range(0,n+1):
            curr=i
            count = 0
            while curr:
                curr = curr & (curr - 1)
                count += 1
            result.append(count)
        return result