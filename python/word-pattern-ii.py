class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        forward = {}
        reverse = {}
        return self.dfs(pattern, str, forward, reverse)
        
    def dfs(self, pattern, str, forward, reverse):       
        if not pattern and not str:
            return True
        if not pattern or not str:
            return False     
        
        c = pattern[0]
        for i in range(1, len(str)-(len(pattern)-1)+1):        
            s = str[:i] 
            if c in forward and forward[c] == s:
                if self.dfs(pattern[1:], str[i:], forward, reverse):
                    return True
            elif c not in forward and s not in reverse:
                forward[c] = s
                reverse[s] = c
                if self.dfs(pattern[1:], str[i:], forward, reverse):
                    return True
                forward.pop(c)
                reverse.pop(s)
        return False
