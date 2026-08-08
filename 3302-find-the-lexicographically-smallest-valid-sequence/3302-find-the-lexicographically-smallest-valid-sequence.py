class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        right_match = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                right_match[j] = i
                j -= 1
        ans = []
        j = 0
        changed = False
        for i in range(n):
            if j == m:
                break            
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and (j + 1 == m or right_match[j + 1] > i):
                ans.append(i)
                changed = True
                j += 1
        return ans if len(ans) == m else []