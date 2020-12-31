class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ans = []
        self.backtracking(S, [], 0)
        return self.ans

    def backtracking(self, S, path, idx):
        if len(path) == len(S):
            self.ans.append("".join(path[:]))
            return

        for i in range(idx, len(S)):
            if S[i].isdigit():
                path.append(S[i])
                self.backtracking(S, path, i+1)
                path.pop()
            else:
                path.append(S[i].lower())
                self.backtracking(S, path, i+1)
                path.pop()
                path.append(S[i].upper())
                self.backtracking(S, path, i+1)
                path.pop()
