class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self, val):
        new_node = Node(val)
        self.first = new_node
        self.last = new_node
        self.length = 1  # Fixed the spelling mistake

    def print_queue(self):
        cur = self.first
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")

    def enqueue(self, val):
        new_node = Node(val)
        if self.first is None:  # When queue is empty
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1  # Ensure length increments in all cases
        return True

    def dequeue(self):
        if self.first is None:  # Queue is empty
            return None
        temp = self.first
        self.first = self.first.next  # Move first to next node
        temp.next = None
        self.length -= 1  # Decrement length
        
        if self.length == 0:  # If queue becomes empty, update last pointer
            self.last = None
        
        return temp.val  # Return the dequeued value

# Testing the corrected queue implementation
que = Queue(1)
que.enqueue(2)
que.enqueue(3)
que.print_queue()

print("Dequeue:", que.dequeue())  # Should remove 1
que.print_queue()

print("Dequeue:", que.dequeue())  # Should remove 2
que.print_queue()

print("Dequeue:", que.dequeue())  # Should remove 3
que.print_queue()

print("Dequeue:", que.dequeue())  # Should return None since queue is empty
