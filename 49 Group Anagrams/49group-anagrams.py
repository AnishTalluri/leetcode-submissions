class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        
        return res.values()


        
        # grouped_anagrams = []
        # used = [False] * len(strs)

        # for i in range(len(strs)):
        #     if used[i]:
        #         continue

        #     anagram = []
        #     anagram.append(strs[i])
        #     used[i] = True

        #     for j in range(i + 1, len(strs)):
        #         if not used[j]:
        #             if sorted(strs[i]) == sorted(strs[j]):
        #                 anagram.append(strs[j])
        #                 used[j] = True
        #     grouped_anagrams.append(anagram)
        # return grouped_anagrams
