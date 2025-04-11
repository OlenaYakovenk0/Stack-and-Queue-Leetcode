class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        data = self.head.data
        self.head = self.head.next
        return data

    @property
    def peek(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.head.data

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s = str(current.data) + ' ' +s
            current = current.next
        return 'bottom -> '+ s+'<- top'

class MyQueue:

    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def push(self, x: int) -> None:
        while not self.pop_stack.is_empty():
            self.push_stack.push(self.pop_stack.pop())
        self.push_stack.push(x)

    def pop(self) -> int:
        while not self.push_stack.is_empty():
            self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self) -> int:
        while not self.push_stack.is_empty():
            self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.peek

    def empty(self) -> bool:
        return self.push_stack.is_empty() and self.pop_stack.is_empty()
