class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=(len(nums)* (len(nums)+1))//2
        total_sum=sum(nums)
        print(f"total {total} and sum: {total_sum} and diff->{total-total_sum}")
        return total-total_sum