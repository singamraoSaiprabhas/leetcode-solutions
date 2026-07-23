class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # n = len(arr)
        # cnt=0
        # for left in range(n):
        #     for right in range(left, n):
        #         current_subarray = arr[left:right + 1]
        #         if sum(current_subarray)%2!=0:
        #             cnt+=1
        # return cnt
        MOD = 10**9 + 7
        
        even_count = 1
        odd_count = 0
        
        current_sum = 0
        total_odd_subarrays = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 0:
                total_odd_subarrays = (total_odd_subarrays + odd_count) % MOD
                even_count += 1
            else:
                total_odd_subarrays = (total_odd_subarrays + even_count) % MOD
                odd_count += 1
                
        return total_odd_subarrays
