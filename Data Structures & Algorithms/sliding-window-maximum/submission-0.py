class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        left = [0] * n
        right = [0] * n

        for i in range(n):
            if i%k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
        right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            if(i + 1)%k ==0:
                right[i] = nums[i]
            else:
                right[i] = max(right[i + 1], nums[i])

        res = []

        for i in range (n-k+1):
            j = i + k - 1
            res.append(max(right[i], left[j]))
        
        return res