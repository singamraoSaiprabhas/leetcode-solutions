class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day_of_year(date: str) -> int:
            month = int(date[:2])
            day = int(date[3:])
            # Sum days of all previous months + current month's days
            return sum(days_in_months[:month - 1]) + day
        
        # Convert all date strings to day-of-year integers
        start_alice = to_day_of_year(arriveAlice)
        end_alice = to_day_of_year(leaveAlice)
        start_bob = to_day_of_year(arriveBob)
        end_bob = to_day_of_year(leaveBob)
        
        # The intersection interval
        overlap_start = max(start_alice, start_bob)
        overlap_end = min(end_alice, end_bob)
        
        # If they overlap, return the difference + 1; otherwise 0
        return max(0, overlap_end - overlap_start + 1)