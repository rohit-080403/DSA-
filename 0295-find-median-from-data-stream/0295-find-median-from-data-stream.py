import heapq
class MedianFinder:

    def __init__(self):
        self.small_max_heap = []
        self.large_min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_max_heap , -num)

        largest_of_small = -heapq.heappop(self.small_max_heap)
        heapq.heappush(self.large_min_heap , largest_of_small)

        if len(self.large_min_heap) > len(self.small_max_heap):
            val_to_move = heapq.heappop(self.large_min_heap)
            heapq.heappush(self.small_max_heap , -val_to_move)




    def findMedian(self) -> float:
        if len(self.small_max_heap) > len(self.large_min_heap):
            return float(-self.small_max_heap[0])

        return (-self.small_max_heap[0] + self.large_min_heap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()