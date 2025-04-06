class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedQueue:
    """A simple linked queue with standard operations only."""

    def __init__(self, iterable=None):
        self._front = self._rear = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.add(item)

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __iter__(self):
        cursor = self._front
        while cursor:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return "[" + ", ".join(map(str, self)) + "]"

    def peek(self):
        if self.isEmpty():
            raise KeyError("Queue is empty.")
        return self._front.data

    def clear(self):
        self._front = self._rear = None
        self._size = 0

    def add(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("Queue is empty.")
        item = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return item


class MyStack:

    def __init__(self):
        self.first_queue = LinkedQueue()
        self.second_queue = LinkedQueue()


    def push(self, x: int) -> None:
        if self.second_queue.isEmpty():
            self.first_queue.add(x)
        else:
            self.second_queue.add(x)

    def pop(self) -> int:
        if self.first_queue.isEmpty() and self.second_queue.isEmpty():
            raise KeyError("Stack is empty.")
        if self.first_queue.isEmpty():
            while len(self.second_queue) > 1:
                self.first_queue.add(self.second_queue.pop())
            return self.second_queue.pop()
        while len(self.first_queue) > 1:
            self.second_queue.add(self.first_queue.pop())
        return self.first_queue.pop()


    def top(self) -> int:
        if self.first_queue.isEmpty() and self.second_queue.isEmpty():
            raise KeyError("Stack is empty.")
        if self.first_queue.isEmpty():
            while len(self.second_queue) > 1:
                self.first_queue.add(self.second_queue.pop())
            top = self.second_queue.peek()
            self.first_queue.add(self.second_queue.pop())
            return top
        while len(self.first_queue) > 1:
            self.second_queue.add(self.first_queue.pop())
        top = self.first_queue.peek()
        self.second_queue.add(self.first_queue.pop())
        return top

    def empty(self) -> bool:
        return self.first_queue.isEmpty() and self.second_queue.isEmpty()


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.empty())

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()