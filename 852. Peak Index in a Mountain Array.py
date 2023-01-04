class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        
        while low <= high :
            mid = (low+high)//2
            if arr[mid] < arr[mid+1]:
                low = mid + 1
            elif arr[mid] > arr[mid+1]:
                high = mid - 1
        return low
          
------------------------------------------------------------------
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i+1] < arr[i]:
                return i
                
-------------------------------------------------------------------

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                return i
