que=[]
def enque():
    element=int(input("enter the elment"))
    que.append(element)
    print(que)
def deque():
    que.pop(0)
    print(que)
def front():
    print(que[0])
def rear():
    print(que[-1])
n=int(input("enter size"))
while True:
    print("enter options 1:enque 2:deque 3:front 4:rear 5:qut")
    choice=int(input("enter the choice"))
    if choice==1:
        enque()
    elif choice==2:
        deque()
    elif choice==3:
        front()
    elif choice==4:
        rear()
    elif choice==5:
        break
    else:
        print("enter valid options")

