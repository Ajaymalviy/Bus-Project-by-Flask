class Node:
    def  __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if self.head:
            self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def print_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <- '
            itr = itr.prev
        print(llstr)


    def getlength(self) :
        if self.head is None:
            print('linkedlist is empty')
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next
        return count    
   


    def insert_at_index(self,index,data):
        if index<0 or index>self.getlength():
            raise Exception('error of invalid exception')
        if index==0:
            self.insert_at_beginning()
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next,itr)
                if node.next:
                    node.next.prev=node
                itr.next=node
                break
            itr=itr.next
            count=count+1   


    def remove_at(self,index):
        if index<0 or index > self.getlength():
            raise Exception('error  of invalid index occure')
        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count +=1
            


# Example usage
dll = DoublyLinkedList()

dll.insert_at_beginning(50)
dll.insert_at_beginning(34)
dll.insert_at_beginning(69)
dll.insert_at_beginning(90)

dll.insert_at_end(111)
dll.insert_at_end(321)
dll.insert_at_end(1000)
dll.insert_at_end(2023)
dll.insert_at_index(2,2)
dll.insert_at_index(3,3)
dll.print_forward()
dll.print_backward()