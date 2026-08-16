class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 建立字典, dict[key].append(value)
        anagram_map = {}

        for s in strs:
            # 建立每個詞對應的key
            key = "".join(sorted(s))
            # 如果這個key以前看過，直接把單字s加進去
            if key in anagram_map:
                anagram_map[key].append(s)
            # 如果沒看過，就在字典裡為它開一個新陣列
            else:
                anagram_map[key] = [s]
        return list(anagram_map.values())