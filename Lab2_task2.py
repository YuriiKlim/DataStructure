def infix_to_postfix(expression):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    for token in expression.split():
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                output.append(top_token)
                top_token = stack.pop()
        else:
            while stack and (priority.get(stack[-1], 0) >= priority[token]):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return ' '.join(output)


expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
print(f"Fix Notation: {expression}")
print(f"Postfix Notation: {infix_to_postfix(expression)}")


def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isnumeric():
            stack.append(int(token))
        else:
            right_operand = stack.pop()
            left_operand = stack.pop()
            if token == '+':
                stack.append(left_operand + right_operand)
            elif token == '-':
                stack.append(left_operand - right_operand)
            elif token == '*':
                stack.append(left_operand * right_operand)
            elif token == '/':
                stack.append(left_operand / right_operand)
            elif token == '^':
                stack.append(left_operand ** right_operand)
    return stack[0]


postfix_expression = infix_to_postfix(expression)
result = evaluate_postfix(postfix_expression)
print(f"Результат обчислення: {result}")
