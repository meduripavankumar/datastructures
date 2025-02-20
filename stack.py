class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0  # Fixed the incorrect initialization

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top  # Point new node to current top
        self.top = new_node  # Update top to the new node
        self.length += 1
        return True

    def pop(self):
        if self.top is None:  # Check if stack is empty
            return None
        temp = self.top
        self.top = self.top.next  # Move top pointer
        temp.next = None  # Break reference
        self.length -= 1
        return temp.val  # Return the popped value

    def peek(self):
        if self.top is None:
            return None
        return self.top.val  # Return value instead of Node object

    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
            return
        cur = self.top
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")

# Testing the corrected stack implementation
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print("Stack after pushes:")
my_stack.print_stack()

print("\nPop:", my_stack.pop())  # Should remove 3
print("Pop:", my_stack.pop())  # Should remove 2
print("Pop:", my_stack.pop())  # Should remove 1
print("Pop:", my_stack.pop())  # Should return None since stack is empty

# Peek should not cause an error
peek_value = my_stack.peek()
if peek_value is not None:
    print("Peek:", peek_value)
else:
    print("Peek: Stack is empty")
