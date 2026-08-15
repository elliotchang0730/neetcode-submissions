class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            # 每次把石頭從大到小排序（reverse=True）
            stones.sort(reverse=True)
            # 出前兩個最重的石頭
            stone1 = stones.pop(0) # 最重
            stone2 = stones.pop(0) # 第二重
            # 如果兩顆石頭重量不一樣，把剩下的大減小差值，丟回陣列
            if stone1 != stone2:
                stones.append(stone1 - stone2)   
        # 如果還剩下一顆石頭，就回傳，如果無，就回傳 0
        return stones[0] if stones else 0
            