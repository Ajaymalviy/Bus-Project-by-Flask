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

