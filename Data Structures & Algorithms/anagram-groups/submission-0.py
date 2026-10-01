class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}

        for i in strs:
            key = ''.join(sorted(i))

            if key not in ana_map:
                ana_map[key] = []

            ana_map[key].append(i)

        return list(ana_map.values())