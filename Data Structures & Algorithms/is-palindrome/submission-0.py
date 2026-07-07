class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s  = s.lower().replace(' ','')
        
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        start = 0
        end = len(s) - 1
        while end > start :
            print(start,end)
            if s[end] != s[start]:
                return False
            start = start + 1
            end = end - 1
        return True