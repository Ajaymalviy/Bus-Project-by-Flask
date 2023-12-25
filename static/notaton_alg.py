expression1=input("enter any exp:")
expression=str(expression1)

def infix_to_postfix(expression):
    stack = []
    postfix = []

    for i in expression:
        if i.isalnum():
            postfix.append(i)
        elif i == '/':
            stack.append(i)
        elif i == '*':
            stack.append(i)
        elif i == '+':
            stack.append(i)
        elif i == '-':
            stack.append(i)
        else:
            