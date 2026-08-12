class Solution:
    def isValid(self, s: str) -> bool:
        # 創建字典，由於stack是後進先出，因此key為右括號
        char_map = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for char in s:
            if char in char_map:
                if stack and stack[-1] == char_map[char]: # 如果配對到
                    stack.pop()
                else:
                    return False # 沒東西配對，或是配對錯了，直接失敗
            else:
                stack.append(char) # 如果不在map的key，則是左括號，直接放入堆疊
        return len(stack) == 0 # 確認配對完

            