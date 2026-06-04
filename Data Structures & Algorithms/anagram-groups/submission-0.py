class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict={}

        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(i)
            else:
                anagram_dict[sorted_word]=[i]
        return list(anagram_dict.values())