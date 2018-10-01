def check_paren(inp):
    paran_map = {'}': '{', ')': '(', ']': '['}
    stack = []

    for char in inp:
        if char in paran_map.keys():
            poped_char = stack.pop()
            if poped_char != paran_map[char]:
                return False
        else:
            stack.append(char)

    if stack:
        return False

    return True

for inp in ["[()]{}{[()()]()}", "[(])"]:
    print check_paren(inp)
