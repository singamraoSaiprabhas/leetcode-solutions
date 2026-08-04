class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt=[]
        for i in range(1,n+1):
            if n%i==0:
                cnt.append(i)
        if len(cnt)<k:
            return -1
        else:
            return cnt[k-1]
        