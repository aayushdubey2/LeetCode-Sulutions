class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        else: 
            stack = []
            pairs = {
                '[' : ']',
                '(' : ')',
                '{' : '}'
            }
            for i in s:
                if i in ['(', '{', '[']:
                    stack.append(i)
                else:
                    if len(stack) == 0 or pairs[stack.pop()] != i:
                        return False
            return len(stack) == 0

        