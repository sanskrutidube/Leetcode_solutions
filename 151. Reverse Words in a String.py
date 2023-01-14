class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        return " ".join(s[::-1])
--------------------------------------------------------------------------151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([ch for ch in reversed(s.split()) if ch])
        
--------------------------------------------------------------------------

