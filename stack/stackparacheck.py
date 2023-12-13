def charcheck(exp):
    stack=[]
    for char in exp:
        if char=='(':
            stack.append(char)
        elif char==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
    return len(stack)==0
exp="("
s=charcheck(exp)
print(s)