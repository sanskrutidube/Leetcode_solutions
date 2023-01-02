class Solution:
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()
        
-----------------------------------------------------------------------

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        word1=word[1:]
        if word.isupper()== True:
            return True
        if word.islower()== True:
            return True
        if word[0].isupper()== True and word1.islower()==True:
            return True
