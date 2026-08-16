class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n # 先建立好 [1, 1, 1, 1....]

        # 計算並儲存每個元素左邊的所有乘積（前綴）
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        # 由右向左，乘上每個元素右邊的所有乘積（後綴）
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
