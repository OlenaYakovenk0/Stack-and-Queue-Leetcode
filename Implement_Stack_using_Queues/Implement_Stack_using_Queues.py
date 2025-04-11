class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        if self.head is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            data = self.head
            self.head = self.head.next
            return data
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.head.data

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.data)+' '
            current = current.next
        return f'start -> {s}<- end'

class MyStack:

    def __init__(self):
        self.first_queue = Queue()
        self.second_queue = Queue()

    def push(self, x: int) -> None:
        if self.second_queue.is_empty():
            self.first_queue.add(x)
        else:
            self.second_queue.add(x)

    def pop(self) -> int:
        if self.first_queue.is_empty() and self.second_queue.is_empty():
            raise KeyError("Stack is empty.")
        if self.first_queue.is_empty():
            while len(self.second_queue) > 1:
                self.first_queue.add(self.second_queue.pop().data)
            return self.second_queue.pop().data
        while len(self.first_queue) > 1:
            self.second_queue.add(self.first_queue.pop().data)
        return self.first_queue.pop().data

    def top(self) -> int:
        if self.first_queue.is_empty() and self.second_queue.is_empty():
            raise KeyError("Stack is empty.")
        if self.first_queue.is_empty():
            while len(self.second_queue) > 1:
                self.first_queue.add(self.second_queue.pop().data)
            top = self.second_queue.peek
            self.first_queue.add(self.second_queue.pop().data)
            return top
        while len(self.first_queue) > 1:
            self.second_queue.add(self.first_queue.pop().data)
        top = self.first_queue.peek
        self.second_queue.add(self.first_queue.pop().data)
        return top

    def empty(self) -> bool:
        return self.first_queue.is_empty() and self.second_queue.is_empty()
