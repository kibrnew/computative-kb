class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counter = Counter(p)
        window = {}
        counts = 0
        left, right = 0, 0
        
        while right < len(s):
            char = s[right]
            if char in p_counter:
                window[char] = window.get(char, 0) + 1
                if window[char] == p_counter[char]:
                    counts += 1
            
            if right - left + 1 > len(p):
                left_char = s[left]
                if left_char in p_counter:
                    if window[left_char] == p_counter[left_char]:
                        counts -= 1
                    window[left_char] -= 1
                left += 1
            
            if counts == len(p_counter):
                result.append(left)
            
            right += 1
        
        return result
                
                