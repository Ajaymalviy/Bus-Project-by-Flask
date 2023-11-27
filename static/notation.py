def operator(char):
    return char in {'+', '-', '*', '/'}

def priority(operator):
    if operator in {'+', '-'}:
        return 1
    elif operator in {'*', '/'}:
        return 2

def infix_to_postfix(expression):
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif operator(char):
            while stack and operator(stack[-1]) and priority(stack[-1]) >= priority(char):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

def solve_postfix(postfix_expression):
    stack = []
    operands = []

    for char in postfix_expression:
        if char.isdigit():
            operands.append(char)
        elif operator(char):
            if operands:
                stack.append(int(''.join(operands)))
                operands = []
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)

    if operands:
        stack.append(int(''.join(operands)))

    return stack[0]
# Given expression
infix_expression = input("Enter a  numerical and  operator containing string :")
# Convert to postfix
postfix_expression = infix_to_postfix(infix_expression)

# Evaluate the postfix expression
result = solve_postfix(postfix_expression)

print(f"The result of the expression {infix_expression} is: {result}")
