class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        right=[]
        equal=[]
        for i in nums:
            if i<pivot:
                left.append(i)
            if i==pivot:
                equal.append(i)
            if i>pivot:
                right.append(i)
        return (left+equal+right)
