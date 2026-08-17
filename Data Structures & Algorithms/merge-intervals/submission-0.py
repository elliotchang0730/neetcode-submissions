class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 依據區間的起點(x[0])進行升冪排序
        intervals.sort(key=lambda x: x[0])
        
        res = []
        
        for interval in intervals:
            # 如果res是空的，或者目前區間的起點大於res最後一個區間的終點
            # 代表完全沒有重疊，直接加進結果
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                # 發生重疊，合併區間，去修改res最後一個區間的終點為兩者最大值
                res[-1][1] = max(res[-1][1], interval[1])
                
        return res