class Stack:
    """Abstract Data Type that defines behavior"""
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack == []:
            return
        last_item = self.stack[-1]
        del self.stack[-1]
        return last_item

    def peek(self):
        if self.stack == []:
            return None
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

stack = Stack()
print(stack.push(1))
print(stack.push(3))
print(stack.push(4))
print(stack.peek())
print(stack.pop())
print(stack.peek())