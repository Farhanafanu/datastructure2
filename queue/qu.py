#using list
# queue=[]
# def enqueue():
#     if len(queue)==n:
#         print("que is full")

#     element=int(input("enter the element"))
#     queue.append(element)
#     print(queue)
# def dequeeu():
#     e=queue.pop(0)
#     print("element deleted is",e)
#     print(queue)
# def display():
#     print(queue)

# n=int(input("enter the size"))
# while True:
#     print("enter the options 1:enque 2:deque 3 :display")
#     choice=int(input("enter the choice"))
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeeu()
#     elif choice==3:
#         display()
#     else:
#         print("enter the valid choice")
# class Que:
#     def __init__(self):
#         self.que=[]
#     def enque(self,item):
#         n=self.que
#         n.append(item)
#     def deque(self):
#         n=self.que
#         if n is None:
#             print("empty")
#         else:
#             n.pop(0)
#     def empty(self):
#         return len(self.que)==0
#     def size(self):
#         return len(self.que)
#     def front(self):
#         print(self.que[0])
#     def rear(self):
        
#         print(self.que[-1])
#     def disply(self):
#         print(self.que)   
# q=Que()
# q.enque(10)
# q.enque(30)
# q.enque(45)
# q.front()
# q.rear()
# # q.deque()
# q.disply()     
#que using list
# que=[]
# def enque():
#     eleemnt=int(input("enter the element"))
#     que.append(eleemnt)
#     print(que)
# def deque():
#     if que:
#         que.pop(0)
#         print(que)
# n=int(input("enter the size"))
# while True:
#     print("enter the options 1:enque 2 deque 3:quet")
#     choice=int(input("enter the choice"))
#     if choice==1:
#         enque()
#     elif choice==2:
#         deque()
#     elif choice==3:
#         break
#     else:
#         print("enter the valid choice")
class Que:
    def __init__(self):
        self.que=[]
    def enque(self,item):
        self.que.append(item)
    def deque(self):
        if self.que:
            self.que.pop(0)
        else:
            print("empty que")
    def front(self):
        print(self.que[0])
    def rear(self):
        print(self.que[-1])
    def display(self):
        print(self.que)
q=Que()
q.enque(65)
q.enque(76)
q.enque(87)
q.deque()
q.front()
q.rear()
q.display()
        