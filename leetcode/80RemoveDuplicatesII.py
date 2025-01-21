def minRemoveToMakeValid1(s: str) -> str:
    if len(s) < 2:
        return ""

    stack = []
    i = 0

    while i < len(s):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if not stack:
                s = s[:i] + s[i + 1:]
            else:
                stack.pop()
        i += 1
    return s

def minRemoveToMakeValid(s: str) -> str:
    indexes_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack:
            indexes_to_remove.add(i)
        else:
            stack.pop()
    indexes_to_remove = indexes_to_remove.union(set(stack))
    string_builder = []
    for i, c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder.append(c)
    return "".join(string_builder)





print(minRemoveToMakeValid("lee(t(c)o)de)"))
print(minRemoveToMakeValid("a)b(c)d"))
print(minRemoveToMakeValid("))(("))