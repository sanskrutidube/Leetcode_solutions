class Solution:
  def maxSubarraySumCircular(self, A: List[int]) -> int:
    totalSum = 0
    currMaxSum = 0
    currMinSum = 0
    maxSum = -math.inf
    minSum = math.inf

    for a in A:
      totalSum += a
      currMaxSum = max(currMaxSum + a, a)
      currMinSum = min(currMinSum + a, a)
      maxSum = max(maxSum, currMaxSum)
      minSum = min(minSum, currMinSum)

    return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)
  -----------------------------------------------------------------------------
  
  class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = nums[0]
        maxi = nums[0]
        currMin = nums[0]
        mini = nums[0]
        for num in nums[1:]:
            currMax = max(num, currMax + num)
            maxi = max(currMax, maxi)
            currMin = min(num, currMin + num)
            mini = min(currMin, mini)
        if sum(nums) == mini:    
            return maxi
        return max(maxi, sum(nums) - mini)
