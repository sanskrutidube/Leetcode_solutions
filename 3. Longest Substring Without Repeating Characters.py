class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        set_ = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            
            while s[r] in set_:
                set_.remove(s[l])
                l += 1
            set_.add(s[r])
            res = max(res, r-l+1)
        
        return res
    ----------------------------------------

    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        mx = left = 0
        for right, c in enumerate(s):
            if c in seen:
                left = max(left, seen[c] + 1)
            seen[c] = right
            mx = max(mx, right-left+1)
        return mx
    ------------------------------------------
   class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        n = len(s)
        start = 0
        ans = 0
        for i in range(n):
            if(s[i] in indexMap and start <= indexMap[s[i]]):
                start = indexMap[s[i]] + 1
            else:
                ans = max(ans,i - start + 1)
            indexMap[s[i]] = i
        return ans
    
    
