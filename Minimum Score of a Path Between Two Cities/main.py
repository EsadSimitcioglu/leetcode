class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        navigation = {}
        for road in roads:
            from_node = road[0]
            to_node = road[1]
            distance = road[2]

            if not (from_node in navigation):
                navigation[from_node] = {}
            navigation[from_node][to_node] = distance

            if not (to_node in navigation):
                navigation[to_node] = {}
            navigation[to_node][from_node] = distance

        visited = set()
        score = float('inf')

        def dfs(n):
            if n in visited or (not n in navigation):
                return
            visited.add(n)
            nonlocal score
            for node in navigation[n]:
                distance_score = navigation[n][node]
                score = min(score, distance_score)
                dfs(node)

        dfs(1)
        return score