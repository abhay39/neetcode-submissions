class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i in strs:
            temp = ''.join(sorted(i))

            if temp not in seen:
                seen[temp] = []

            seen[temp].append(i)
        return list(seen.values())