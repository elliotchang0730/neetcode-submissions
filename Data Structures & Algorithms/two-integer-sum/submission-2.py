class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 雙重迴圈暴力解
        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):
                if nums[i] + nums[y] == target:
                    return [i, y]
        """

        # 字典(雜湊表)方法
        # 建立一本筆記本：Key 記數字，Value 記索引的位置
        num_map = {}
        for i in range(len(nums)):
            current_num = nums[i]
            needed = target - current_num
            if needed in num_map:
                # 如果有看過，回傳以前那個數字的位置以及現在的位置
                return [num_map[needed], i]
            # 沒看過，登記到筆記本裡
            num_map[current_num] = i