class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted(map(str,nums), key=lambda s:s*9)[::-1])))
