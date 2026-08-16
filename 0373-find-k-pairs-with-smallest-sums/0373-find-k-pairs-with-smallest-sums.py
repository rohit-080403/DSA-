import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        result = []

        for i in range(min(k , len(nums1))):
            initial_sum = nums1[i] + nums2[0]
            heapq.heappush(min_heap , (initial_sum , i,0))
        
        while min_heap and len(result) < k:
            curr_sum , i , j = heapq.heappop(min_heap)

            result.append([nums1[i] , nums2[j]])

            if j+1 < len(nums2):
                next_sum  = nums1[i] + nums2[j+1]
                heapq.heappush(min_heap , (next_sum , i , j+1))
        return result