class Solution:
    
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        l = len(hand)
        
        # input checks
        if W == 0 or l == 0:
            return False
        
        counts = {}
        for i in hand:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        
        for k in sorted(counts):
            #print(counts , "\n")
            while counts[k] > 0:
                groupCount = 0
                for i in range(W):
                    if k+i in counts and counts[k+i] > 0:
                        counts[k+i] -= 1
                        groupCount += 1
                if groupCount < W:
                    return False
        
        return True
            

s = Solution()
ll = [1,2,3,6,2,3,4,7,8]
W=3
print(ll, W, s.isNStraightHand(ll, W))

ll = [1,2,3,4,5]
W=4
print(ll, W, s.isNStraightHand(ll, W))

ll = [1,1,2,2,3,3]
W = 3
print(ll, W, s.isNStraightHand(ll, W))

ll = [8,6,5,7,9]
W = 5
print(ll, W, s.isNStraightHand(ll, W))