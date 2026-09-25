class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(city):
            visited.add(city)
            for nei in range(n):
                if isConnected[city][nei] == 1 and nei not in visited:
                    dfs(nei)
        for city in range(n):
            if city not in visited:
                count +=1
                dfs(city)

        return count

