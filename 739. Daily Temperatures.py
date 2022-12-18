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
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res, stack = [0] * len(T), []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                res[stack.pop()] = i - stack[-1]
            stack.append(i)
        return res
