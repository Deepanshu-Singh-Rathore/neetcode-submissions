class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        var=set()
        result = False
        for i in nums:
            if i in var:
                result = True
                break
            else:
                var.add(i)
        return result
        