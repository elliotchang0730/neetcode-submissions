class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        """ 直覺寫法如下
        new_s = "".join(char.lower() for char in s if char.isalnum())
        return new_s == new_s[::-1]
        """
        
        # 指標寫法
        l = 0
        r = len(s) - 1 # 右指標從最右邊開始

        while l < r:
            while l < r and not s[l].isalnum():
                #左指標非標點符號空格，則繼續往右
                l += 1
            while l < r and not s[r].isalnum():
                #右指標非標點符號空格，則繼續往左
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
