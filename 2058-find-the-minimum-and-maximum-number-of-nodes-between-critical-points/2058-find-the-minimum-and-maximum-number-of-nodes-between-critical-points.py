# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        min_dist = float('inf')
        first_crit_idx = -1
        prev_crit_idx = -1

        prev = head
        curr = head.next
        idx = 1

        while curr.next:
            nxt = curr.next
            
            # Check if current node is a local maxima or minima
            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):
                
                if first_crit_idx == -1:
                    # First critical point found
                    first_crit_idx = idx
                else:
                    # Calculate min distance with the previously found critical point
                    min_dist = min(min_dist, idx - prev_crit_idx)
                
                # Update the previous critical point index to the current one
                prev_crit_idx = idx

            # Move pointers forward
            prev = curr
            curr = nxt
            idx += 1

        # If min_dist is still infinity, we found fewer than 2 critical points
        if min_dist == float('inf'):
            return [-1, -1]

        # Max distance is always the difference between the last and first critical points found
        max_dist = prev_crit_idx - first_crit_idx
        
        return [min_dist, max_dist]