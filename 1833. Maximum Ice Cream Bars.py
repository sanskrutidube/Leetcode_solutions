class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs=sorted(costs)
        count=0
        for i in costs:
            if i<=coins:
                count+=1
                coins=coins-i
        return count
