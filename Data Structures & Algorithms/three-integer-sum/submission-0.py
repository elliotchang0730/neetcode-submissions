class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # 重新排序，例如[1,0,-1,3]變成[-1,0,1,3]
        n = len(nums)

        for i in range(n):
            # 如果目前最小的數已經大於0，後面再怎麼加都不可能等於0，因為無負數
            if nums[i] > 0:
                break
            # 防止答案重複，例如[-1,-1,0,1]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            L = i + 1
            R = n - 1

            while L < R:
                current_sum = nums[i] + nums[L] + nums[R]

                if current_sum == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 找到解後，跳過L的重複元素
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    # 找到解後，跳過R的重複元素
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1

                    L += 1
                    R -= 1
                
                elif current_sum < 0:
                    L += 1 # 總和太小，左指標右移
                else:
                    R -= 1 # 總和太大，右指標左移
        return res
