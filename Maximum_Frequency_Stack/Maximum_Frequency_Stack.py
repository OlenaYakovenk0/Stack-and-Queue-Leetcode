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

class FreqStack:
    def __init__(self):
        self.val_to_freq = {}
        self.freq_to_stack = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.val_to_freq.get(val, 0) + 1
        self.val_to_freq[val] = freq

        if freq > self.max_freq:
            self.max_freq = freq

        if freq not in self.freq_to_stack:
            self.freq_to_stack[freq] = Stack()

        self.freq_to_stack[freq].push(val)

    def pop(self) -> int:
        most_freq_stack = self.freq_to_stack[self.max_freq]
        val = most_freq_stack.pop()
        self.val_to_freq[val] -= 1

        if most_freq_stack.is_empty():
            self.max_freq -= 1

        return val


# FreqStack freqStack = new FreqStack();
stack = FreqStack()
print(stack)
# freqStack.push(5); // The stack is [5]
stack.push(5)
# freqStack.push(7); // The stack is [5,7]
stack.push(7)
print(stack)
# freqStack.push(5); // The stack is [5,7,5]
stack.push(5)
print(stack)
# freqStack.push(7); // The stack is [5,7,5,7]
stack.push(7)
print(stack)
# freqStack.push(4); // The stack is [5,7,5,7,4]
stack.push(4)
print(stack)
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
stack.push(5)
print(stack)
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
print(stack.pop())
print(stack)
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
print(stack.pop())
print(stack)
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
print(stack.pop())
print(stack)
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
print(stack.pop())
print(stack)