class Solution:
    def findJudge(self, N, trust):
        trusted = [0] * (N+1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1
        for i in range(1, N+1):
            if trusted[i] == N-1:
                return i
        return -1
-----------------------------------------------------------------


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_to, trusted = defaultdict(int), defaultdict(int)

        for a, b in trust:
            trust_to[a] += 1
            trusted[b] += 1
        
        for i in range(1, n+1):
            if trust_to[i] == 0 and trusted[i] == n - 1:
                return i
        
        return -1
----------------------------------------------------------------------


