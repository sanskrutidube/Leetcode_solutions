class Solution:
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans
-------------------------------------------------------

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        result = [0] * l
        for i in range(l-1):
            for j in range(i+1, l):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        return result
