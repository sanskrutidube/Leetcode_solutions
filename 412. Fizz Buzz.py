class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['FizzBuzz' if i%15 == 0 else 'Buzz' if i%5 == 0 else 'Fizz' if i%3 == 0 else str(i) for i in range(1,n+1)]
-----------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["Fizz"*(d%3==0)+"Buzz"*(d%5==0) or f"{d}" for d in range(1,n+1)]
