class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        self.backtracking(n+1, [], 1,set())
        return self.ans

    def backtracking(self, n, path, idx,visited):
        if len(path) == n-1:
            self.ans += 1
            return
        for i in range(1, n):
            if i in visited:
                continue
            if i % (len(path)+1) == 0 or (len(path) + 1) % i == 0:
                path.append(i)
                visited.add(i)
                self.backtracking(n, path, i+1,visited)
                path.pop()
                visited.remove(i)
