class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # [count,blocker]
        r,d = 0,0
        count = 0
        senate = [x for x in senate]
        r_count,d_count = 0,0
        for i in senate:
            if i is 'R':
                r_count +=1
            else:
                d_count +=1
        while r_count > 0 and d_count> 0:
            index = count % len(senate)
            if senate[index] is 'R':
                if d > 0:
                    senate[index] = 'X'
                    d-=1
                    r_count -=1
                else:
                    r+=1
            elif senate[index] is 'D':
                if r > 0:
                    senate[index] = 'X'
                    d_count -=1
                    r-=1
                else:
                    d+=1
            count+=1
        r,d = 0,0
        for i in senate:
            if i is 'R':
                r+=1
            elif i is 'D':
                d+=1
        if r > d:
            return "Radiant"
        else:
            return "Dire"
                
            
            
        