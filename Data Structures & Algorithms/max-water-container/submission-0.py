class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areamap = {}
        l, r = 0, len(heights) - 1
        while l<r:
            min_val = min(heights[l], heights[r])
            dis = r - l
            area = min_val * dis

            areamap[(l, r)] = area

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max(areamap.values())