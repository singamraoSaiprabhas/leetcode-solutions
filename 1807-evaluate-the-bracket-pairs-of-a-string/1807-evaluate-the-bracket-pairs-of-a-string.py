class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {k: v for k, v in knowledge}
        
        result = []
        curr_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(curr_key)
                # Replace with the value if found, otherwise '?'
                result.append(d.get(key_str, '?'))
                curr_key = []
            elif in_bracket:
                curr_key.append(char)
            else:
                result.append(char)
                
        return "".join(result)