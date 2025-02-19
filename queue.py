class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self,val):
        new_node = Node(val)
        self.first = None
        self.last = None
        self.legnth =1

    def print_queue(self):
        cur = self.first
        while cur:
            print(cur.val)
            cur = cur.next

    def enqueue(self,val):
        new_node = Node(val)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.legnth +=1
            return True
        self.last.next = new_node
        self.last = new_node
        self.legnth +=1
        return True
    
    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        self.first = temp.next
        temp.next = None
        self.legnth -=1
      
        return temp

que = Queue(1)
que.enqueue(2)
que.enqueue(3)
que.print_queue()
print("dequeue")
que.dequeue()
que.print_queue()


