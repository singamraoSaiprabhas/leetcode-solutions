import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            # Find where x would be inserted to maintain sorted order
            idx = bisect.bisect_left(arr2, x)
            
            # The closest elements in arr2 to x will be at idx and idx - 1
            is_valid = True
            
            # Check the element right at or after the insertion point
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                is_valid = False
                
            # Check the element right before the insertion point
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                is_valid = False
                
            if is_valid:
                distance_value += 1
                
        return distance_value