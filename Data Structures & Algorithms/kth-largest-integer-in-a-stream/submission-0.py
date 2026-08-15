class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # 陣列轉化為最小heap結構
        heapq.heapify(self.heap)

        """
        例如[1, 2, 3, 4],
        求第3大, 踢出1, 得到2是第3大
        加入5, [2, 3, 4, 5], 踢出2, 得到3是第3大
        加入6, [3, 4, 5, 6], 踢出3, 得到4是第3大
        因次heap每次總數不會超過3就能到第3大。
        """
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # 根據最小heap，heap[0] 永遠是籃子裡最小的
        # 因為籃子裡裝的是最強的k個，最強裡面的最弱，就是「第k大」
        return self.heap[0]
        
