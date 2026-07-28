class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        st=0
        end=len(people)-1
        cnt=0
        while st <=end:
            if people[st]+people[end]<=limit:
                st+=1
                end-=1
            else:
                end-=1
            cnt+=1

        return cnt 