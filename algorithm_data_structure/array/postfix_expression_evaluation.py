def evaluate_postfix_expr(expression):
    result_stack = []
    for char in expression.split(' '):
        if char in ['*', '-', '/', '+']:
            operand1 = result_stack.pop()
            operand2 = result_stack.pop()
            if char == '-':
                result = int(operand2) - int(operand1)
            elif char == '*':
                result = int(operand2) *  int(operand1)
            elif char == '/':
                result = int(operand2) /  int(operand1)
            elif char == '+':
                result = int(operand2) + int(operand1)
                
            result_stack.append(result)
        else:
            result_stack.append(char)
    return result_stack.pop()

expr = "2 3 1 * + 9 -"
print evaluate_postfix_expr(expr)

