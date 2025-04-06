class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedStack:
    def __init__(self, iterable=None):
        self._items = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        return "[" + ", ".join(map(str, self)) + "]"

    def __iter__(self):
        def visitNodes(node):
            if node:
                yield from visitNodes(node.next)
                yield node.data
        return visitNodes(self._items)

    def peek(self):
        if self.isEmpty():
            raise KeyError("Stack is empty.")
        return self._items.data

    def clear(self):
        self._items = None
        self._size = 0

    def push(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("Stack is empty.")
        item = self._items.data
        self._items = self._items.next
        self._size -= 1
        return item


class MyQueue:

    def __init__(self):
        self.push_stack = LinkedStack()
        self.pop_stack = LinkedStack()


    def push(self, x: int) -> None:
        while not self.pop_stack.isEmpty():
            self.push_stack.push(self.pop_stack.pop())
        self.push_stack.push(x)


    def pop(self) -> int:
        while not self.push_stack.isEmpty():
            self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.pop()


    def peek(self) -> int:
        while not self.push_stack.isEmpty():
            self.pop_stack.push(self.push_stack.pop())
        return self.pop_stack.peek()


    def empty(self) -> bool:
        return self.push_stack.isEmpty() and self.pop_stack.isEmpty()
