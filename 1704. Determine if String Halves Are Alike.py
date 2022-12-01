class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        a=0
        vowels = "aeiouAEIOU"
        for i in s[:l//2]:
            if i in vowels:

                a+=1
        for i in s[(l//2):]:
            if i in vowels:
                a-=1
        return a==0
      
---------------------------------------------------------
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt, half = 0, len(s) / 2
        for i, c in enumerate(s):
            if c in "aeiouAEIOU":
                cnt += 1 if i < half else -1 
        return cnt == 0
----------------------------------------------------------
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        count = 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                count+=1
            if s[-i-1] in vowels:
                count-=1

        return count == 0
------------------------------------------------------------

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        a_vowels=[]
        b_vowels=[]
        for i in a:
            if i in ('a','e','i','o','u','A','E','I','O','U'):
                a_vowels.append(i)
        for j in b:
            if j in ('a','e','i','o','u','A','E','I','O','U'):
                b_vowels.append(j)
        return(len(a_vowels) == len(b_vowels))
           
 --------------------------------------------------------------
