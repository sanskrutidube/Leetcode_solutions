class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lst="abcdefghijklmnopqrstuvwxyz"
        for i in lst:
            if i not in sentence:
                return False
        return True
