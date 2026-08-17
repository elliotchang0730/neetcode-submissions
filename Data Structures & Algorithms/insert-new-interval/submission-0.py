class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        # 將所有完全在newInterval左邊且不重疊的區間加入res
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # 當發生重疊時，不斷合併區間，更新newInterval的邊界
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # 把合併完的最大newInterval放進res
        res.append(newInterval)
        
        # 將剩下完全在右邊不重疊的區間通通丟進res
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res