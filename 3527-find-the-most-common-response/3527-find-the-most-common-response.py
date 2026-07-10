class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counts = Counter()
        for day in responses:
            unique_responses_today = set(day)
            for response in unique_responses_today:
                counts[response] += 1
        best_response = min(counts.keys(), key=lambda k: (-counts[k], k))
        
        return best_response