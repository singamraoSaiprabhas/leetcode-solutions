from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            curr = queue.popleft()

            if is_valid(curr):
                result.append(curr)
                found = True

            # If we already found valid strings at this level,
            # don't generate the next level (which would have more removals).
            if found:
                continue

            for i, char in enumerate(curr):
                if char not in ('(', ')'):
                    continue

                # Generate neighbor by removing curr[i]
                nxt = curr[:i] + curr[i + 1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result