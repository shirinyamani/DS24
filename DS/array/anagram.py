class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False    
        mapping = {}
        for char in s:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

        for char in t:
            if char in mapping:
                mapping[char] -= 1
            else:
                return False
        for c in mapping.values():
            if c != 0:
                return False
            
        return True

