class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        s= list(s)
        g= list(goal)
        for i in range(len(s)):
            first=s[0]
            s.pop(0);s.append(first)
            if s == g:
                return True
        return False

-----------------------------------------------------------

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal+goal 
        
------------------------------------------------------------

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[0:i] == goal:
                return True
