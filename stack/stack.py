stack=[]
def push():
    element=int(input("enter element"))
    stack.append(element)
    print(stack)
def pop():
    stack.pop()
    print(stack)
n=int(input("enter size"))
while True:
    print("enter the options 1:push 2:pop 3:quit")
    choice=int(input("enter choice"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter valid choice")