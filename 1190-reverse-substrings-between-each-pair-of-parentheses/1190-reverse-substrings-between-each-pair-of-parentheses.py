class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                segment = []
                while stack and stack[-1] != '(':
                    segment.append(stack.pop())
                stack.pop()  # Remove '('
                stack.extend(segment)
            else:
                stack.append(char)
                
        return "".join(stack)