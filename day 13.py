# s = []
# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')

# print (s.pop())
# print (s.pop())
# print (s.pop())
# print (s.pop())
# print (s.pop())


# Implement a stack with push, pop, and peek ?

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Add item to top of stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return top item
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return top item without removing
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top item:", stack.peek())  # Output: 30
print("Popped item:", stack.pop())  # Output: 30
print("Top item after pop:", stack.peek())  # Output: 20
