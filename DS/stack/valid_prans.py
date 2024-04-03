class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []
        for p in s:
            if p in pairs:
                stack.append(p)
            elif stack and pairs[stack.pop()] == p:
                continue
            else:
                return False  # Corrected to return False here
        return len(stack) == 0


#### solution 2: SET

def valid_(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    opennig = set('({[')
    match = set([('{','}'),('[',']'),('(',')')])

    for p in s:
        if p in opennig:
            stack.append(p)

        else:

            if len(stack) == 0:
                return False
            
            last_open = stack.pop()
            
            if (last_open, p) not in match:
                return False
    return len(stack) == 0

        
#NOTE:TAKEOUT: 1. USE SET for search or check purposes

