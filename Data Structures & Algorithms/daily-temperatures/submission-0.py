class Solution:
    def dailyTemperatures(self, t1: List[int]) -> List[int]:
        n = len(t1)
        ans = [0]*n
        stack = []
        for i, temp in enumerate(t1):
            while stack and temp >t1[stack[-1]]:
                prev_ind = stack.pop()
                ans[prev_ind] = i - prev_ind
            stack.append(i)
        return ans