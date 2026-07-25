class Solution:
    def maxProduct(self, n: int) -> int:
        first=0;second=0
        while n>0:
            x=n%10
            if x>first:
                second=first
                first=x
            elif x>second:
                second=x
            n=n//10
        return int(first * second)