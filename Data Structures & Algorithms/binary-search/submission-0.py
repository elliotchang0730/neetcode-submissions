class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # 當l和r重合時，那個點也必須檢查
        while l <= r:
            # 計算中間點的索引
            mid = (l + r) // 2
            # 中間值剛好就是target，直接回傳它的索引mid
            if nums[mid] == target:
                return mid
            # 中間值太大了，代表target在左半邊
            elif nums[mid] > target:
                r = mid - 1
            # 中間值太小了，代表target在右半邊
            else:
                l = mid + 1
        # 如果整個迴圈走完都沒觸發return mid，代表根本找不到target
        return -1

            
            
        