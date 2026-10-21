class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t)> len(s):return ""

        counts = {}

        for c in t:
            counts[c] = counts.get(c, 0) + 1

        window = {}
        shim, nik = 0, len(counts)
        res, min_len = "", len(s)+1

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0)+1

            if c in counts and window[c] == counts[c]:
                shim += 1

            while shim == nik:
                if(right - left + 1)< min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1
                if left_char in counts and window[left_char] < counts[left_char]:
                    shim -= 1
                left += 1
        return res 
            