class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                r,l=stack.pop(),stack.pop()
                if i== "+":
                    stack.append(l+r)
                if i=="-":
                    stack.append(l-r)
                if i=="*":
                    stack.append(l*r)
                if i=="/":
                    stack.append(int(float(l)/r))
        res= stack.pop()
        return res
