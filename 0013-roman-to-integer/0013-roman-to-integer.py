class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        p=0;tot=0
        while p<len(s):
            if p+1<len(s) and d[s[p]]<d[s[p+1]]:
                tot+=d[s[p+1]]-d[s[p]]
                p+=2
            else:
                tot+=d[s[p]]
                p+=1
        return tot