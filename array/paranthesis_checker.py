def check_for_parenthesis(expr):
    stack = []
    paran_map = {')': '(', '}': '{', ']': '['}
    balanced = True
    for char in expr:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            poped_char = stack.pop()
            #import pdb;pdb.set_trace()
            if poped_char != paran_map.get(char):
                return False
    
    if stack:
        return False
    return balanced

for inp in ["[()]{}{[()()]()}", "[(])"]:
    print inp
    print check_for_parenthesis(inp)

