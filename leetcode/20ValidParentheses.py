class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        for i, c in enumerate(s):
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue

            if len(stack) == 0:
                return False

            popped = stack.pop()
            if popped == '(' and c != ')' or popped == '{' and c != '}' or popped == '[' and c != ']':
                return False

        return len(stack) == 0