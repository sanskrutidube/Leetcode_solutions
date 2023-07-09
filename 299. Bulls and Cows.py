class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s=list(secret)
        g=list(guess)
        bulls=0
        for i in range(len(s)):
            if s[i]==g[i]:
                bulls+=1
        cows=0
        for i in set(s):
            cows += min(s.count(i), g.count(i))

        ans= "{}A{}B".format(bulls,cows-bulls)
        return ans
