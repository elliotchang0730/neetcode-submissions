# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # 一開始前面沒東西
        curr = head # 頭節點

        while curr:
            nxt = curr.next # 儲存頭節點的下個節點
            curr.next = prev # 反轉箭頭指向前面

            # 處理下個節點
            prev = curr # prev往前移到curr的位置
            curr = nxt # curr往前移到nxt的位置
        
        return prev

        """ 簡化
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
        """
       
        
        