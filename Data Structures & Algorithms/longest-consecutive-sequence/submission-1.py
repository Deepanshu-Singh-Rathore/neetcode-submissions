class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        res = 0
# sequence check and length update
        for _ in nums:
    #next num in seq
            if _ in set_num and (_ - 1) not in set_num:
                pointer = _
                count = 0
                while pointer in set_num:
                    pointer +=1
                    count +=1
                    res = max(res, count)
        return res