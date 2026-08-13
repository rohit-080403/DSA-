from collections import Counter 
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_count = Counter(nums)
        unique_pairs = 0

        for num in num_count:
            if k>0:
                if num + k in num_count:
                    unique_pairs +=1
            else:
                if num_count[num] > 1:
                    unique_pairs +=1
        return unique_pairs