class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse_expr(i: int):
            # An expression is a union of terms separated by commas
            res = set()
            term_set, i = parse_term(i)
            res.update(term_set)
            
            while i < len(expression) and expression[i] == ',':
                term_set, i = parse_term(i + 1)
                res.update(term_set)
                
            return res, i

        def parse_term(i: int):
            # A term is a concatenation of factors
            res = {""}
            while i < len(expression) and (expression[i].isalpha() or expression[i] == '{'):
                factor_set, i = parse_factor(i)
                # Cartesian product for concatenation
                res = {u + v for u in res for v in factor_set}
                
            return res, i

        def parse_factor(i: int):
            # A factor is either a single letter or { expression }
            if expression[i] == '{':
                res, i = parse_expr(i + 1)
                return res, i + 1  # Add 1 to skip the closing '}'
            else:
                return {expression[i]}, i + 1
        
        # Parse the entire expression starting at index 0
        result_set, _ = parse_expr(0)
        
        # The problem asks for the sorted list of words
        return sorted(list(result_set))