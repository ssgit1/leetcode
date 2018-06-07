class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        funcTimes = [0] * n
        stack = []
        prev = 0
        for event in logs:
            (fid, call, t) = event.split(':')
            fid = int(fid)
            t = int(t) 
            if call == 'start':
                funcTimes[fid] += 1  
                if stack:
                    funcTimes[stack[-1]] += (t - prev - 1)
                stack.append(fid)
                prev = t + 1
            elif call == 'end':
                funcTimes[stack[-1]] += (t - prev + 1)
                stack.pop()
                prev = t
            
        return funcTimes
