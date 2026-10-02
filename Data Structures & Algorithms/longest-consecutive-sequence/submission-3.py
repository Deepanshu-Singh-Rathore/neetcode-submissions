class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0
# sequence check and length update
        for num in set_nums:
    #next num in seq
            if (num - 1) not in set_nums:
                count = 0
                while num + count in set_nums:
                    count +=1
                    res = max(res, count)
        return res