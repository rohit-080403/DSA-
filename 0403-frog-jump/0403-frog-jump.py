class Solution:
    def canCross(self, stones: list[int]) -> bool:
        stone_set = set(stones)
        last = stones[-1]

        memo = {}

        def dfs(pos , jump):
            if pos == last:
                return True

            if (pos , jump) in memo:
                return memo[(pos , jump)]
            
            for next_jump in (jump-1 , jump , jump+1):
                if next_jump <= 0:
                    continue
                next_pos = pos + next_jump

                if next_pos in stone_set:
                    if dfs(next_pos , next_jump):
                        memo[(pos , jump)] = True
                        return True
            memo[(pos , jump)] = False
            return False
        return dfs(0 , 0)