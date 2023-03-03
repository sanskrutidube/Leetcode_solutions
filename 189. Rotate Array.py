#Solution 1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            a=nums.pop()
            nums.insert(0,a)

#Solution 2 - most optimal out of the three
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if len(nums) > 1 and  k > 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]

#Solution 3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)                   
        nums[:] = nums[-k:] + nums[:-k] 
