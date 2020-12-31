# Union Find
class UnionFind:
    def __init__(self):
        self.uf = {}
    def find(self, x):
        if not x in self.uf:
            self.uf[x] = x
        if self.uf[x] == x:
            return x
        return self.find(self.uf[x])
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.uf[root_x] = root_y
        return True

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False

        uf = UnionFind()
        for pair in pairs:
            uf.union(pair[0], pair[1])
        for word1, word2 in zip(words1, words2):
            if uf.find(word1) != uf.find(word2):
                return False
        return True



# DFS solution
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        graph = collections.defaultdict(list)
        for pair in pairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            visited = set()
            if word1 != word2 and not self.dfs(graph, word1, word2, visited):
                return False
        return True

    def dfs(self, graph, src, dst, visited):
        if src == dst: return True
        visited.add(src)
        for nei in graph[src]:
            if not nei in visited:
                if self.dfs(graph, nei, dst, visited):
                    return True
        return False

