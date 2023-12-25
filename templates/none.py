from collections import deque
# a=[1,2,3]
# b=deque([1,3])
# print(dir(a))
# print(dir(b))
# class Stack:
#     def __init__(self) -> None:
#         self.container=deque()
#     def push(self,val):
#         self.container.append(val)
#     def peek(self):
#         return self.container[-1]
#     def pop(self):
#         return self.container.pop()
#     def size(self):
#         return len(self.container)
# stack=Stack()    
# string="codemos"
# for i in range(len(string)):
#     stack.push(i)


class Stack:
    list=[]
    def __init__(self) -> None:
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def peek(self):
        return self.container[-1]
    def pop(self):
        return self.container.pop()
    def size(self):
        return len(self.container)
    

s = Stack()
for i in range(5):
    print("enter number" ,i,":")
    s.push()
  
    
