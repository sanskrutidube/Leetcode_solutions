class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        for i in c1:
            for j in c2:
                new_c1 = c1 - Counter({i: 1}) + Counter({j: 1})
                new_c2 = c2 + Counter({i: 1}) - Counter({j: 1})
                if len(new_c1) == len(new_c2): 
                    return True
        return False
