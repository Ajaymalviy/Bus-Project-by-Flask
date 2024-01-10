from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def peek(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def display(self):
        return self.container
    

#-------------------------------------------------------------------
    def find_min_element(self):
        if len(self.container)==0:
            return "empty"
        min=self.container[0]
        for i in self.container:
            if i < min:
                min=i
        return min   

#---------------------------------------------------------------
    def sort_ascending(self):
        temp_stack = Stack()

        while self.size() > 0:
            # Pop the top element from the original stack
            current_element = self.pop()

            # Move elements from the temporary stack to the original stack
            while temp_stack.size() > 0 and temp_stack.peek() > current_element:
                self.push(temp_stack.pop())

            # Push the current element onto the temporary stack
            temp_stack.push(current_element)

        # Move the remaining elements from the temporary stack to the original stack
        while temp_stack.size() > 0:
            self.push(temp_stack.pop())
   

stack = Stack()
stack.push(14)
stack.push(5)
stack.push(8)
stack.push(10)
stack.push(11)
stack.push(9)
stack.push(13)
stack.push(2)
print('\nstack :', stack.display())

print( '\nminimum element',stack.find_min_element())
      
# print('size : ', stack.size())
# print('peek : ', stack.peek())  
# print('pop : ', stack.pop())    
# print('size : ', stack.size())   



class MinStack:

    def __init__(self):
        # Stack to store elements
        self.stack = []
        # Stack to store minimum values
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the element onto the main stack
        self.stack.append(val)
        
        # Update the minimum stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # Pop the element from the main stack
            popped_element = self.stack.pop()
            
            # If the popped element is the current minimum, pop from the minimum stack
            if popped_element == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            # Return the top element of the main stack
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            # Return the current minimum from the minimum stack
            return self.min_stack[-1]
