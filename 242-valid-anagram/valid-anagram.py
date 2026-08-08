class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = [0] * 26

        for c in s:
            arr[ord(c) - ord('a')] += 1

        for c in t:
            arr[ord(c) - ord('a')] -= 1
        
        return all(x == 0 for x in arr)