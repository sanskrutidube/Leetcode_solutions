class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                
------------------------------------------------------------------------

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def bubblesort(nums):
            n=len(nums)
            for i in range(n):
                for j in range(n-i-1):
                    if nums[j]>nums[j+1]:
                        nums[j], nums[j+1]=nums[j+1],nums[j]
        bubblesort(nums)
        
        
-------------------------------------------------------------------------

class Solution:
    def sortColors(self, nums):
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2
        
---------------------------------------------------------------------------
