class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 建立字典, dict[key].append(value)
        anagram_map = defaultdict(list)

        for s in strs:
            # 字串排列
            sorted_list = sorted(s)
            # 拼回字串
            key = "".join(sorted_list)
            # 將字串塞入對應的key
            anagram_map[key].append(s)
        # 回傳值
        return list(anagram_map.values())