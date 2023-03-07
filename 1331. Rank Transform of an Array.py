class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        cnt = 1
        for i in sorted(list(set(arr))):
            rank[i] = cnt
            cnt += 1
        return [rank[i] for i in arr]
---------------------------------------------------------------------

class Solution:
    def arrayRankTransform(self, arr):
        ranks = {}
        for rank, num in enumerate(sorted(set(arr))):
            ranks[num] = rank+1
        return [ranks[num] for num in arr]
