class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}
        result = []

        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1

        sorted_items = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        for item, frequency in sorted_items[:k]:
            result.append(item)

        return result