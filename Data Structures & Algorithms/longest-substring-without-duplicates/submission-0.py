class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() # 紀錄目前視窗的字母
        L = 0 # 左指標
        max_len = 0 # 紀錄最大長度

        # R是右指標，不斷往右擴張
        for R in range(len(s)):
            # 如果發現s[R]重複，左指標L縮小視窗，直到不重複
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            # 將新字母加入視窗
            char_set.add(s[R])

            # 計算目前視窗的長度，並更新最大值
            max_len = max(max_len, R - L + 1)
        return max_len