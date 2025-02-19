class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length =1

    def push(self,val):
        new_node = Node(val)
        if self.top is None:
            self.top = new_node
            self.length +=1
            return True
        new_node.next = self.top
        self.top = new_node
        self.length +=1
        return True

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -=1
        return temp

    def peek(self):
        if self.top is None:
            return None
        return self.top

    def print_stack(self):
        if self.top is None:
            return None
        cur = self.top
        while cur:
            print(cur.val)
            cur = cur.next

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.print_stack()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.peek().val)
    


        
