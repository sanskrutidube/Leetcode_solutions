class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return not num or num % 10
      
----------------------------------------------------------

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        return True
