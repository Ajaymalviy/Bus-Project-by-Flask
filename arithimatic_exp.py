def solution_for_arithmatic_expression(expression):

    operators = {'+', '-', '*', '/'}
    stack_of_operand = []
    stack_of_operator = []
    
    def apply_operator(operator, stack_of_operand):
        if len(stack_of_operand) < 2:
            raise ValueError("Invalid expression")

        operand2 = stack_of_operand.pop()
        operand1 = stack_of_operand.pop()

        if operator == '+':
            stack_of_operand.append(operand1 + operand2)
        elif operator == '-':
            stack_of_operand.append(operand1 - operand2)
        elif operator == '*':
            stack_of_operand.append(operand1 * operand2)
        elif operator == '/':
            if operand2 == 0 or operand1 % operand2 != 0:
                raise ValueError("Division by zero or result is not an integer")
            stack_of_operand.append(operand1 // operand2)


    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            stack_of_operand.append(int(expression[i:j]))
            i = j
        elif expression[i] in operators:
            stack_of_operator.append(expression[i])
            i += 1
        else:
            i += 1

    while stack_of_operator:
        apply_operator(stack_of_operator.pop(), stack_of_operand)

    if len(stack_of_operand) != 1:
        raise ValueError("Invalid expression")

    return stack_of_operand[0]

# Example usage:
expression = input("Enter an arithmetic expression: ")
try:
    result = solution_for_arithmatic_expression(expression)
    print(f"Result of '{expression}' is: {result}")
except ValueError as e:
    print(f"Error: {e}")
