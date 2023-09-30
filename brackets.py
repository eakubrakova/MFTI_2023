def brackets(line):
    stack = []
    
    for char in line:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False
