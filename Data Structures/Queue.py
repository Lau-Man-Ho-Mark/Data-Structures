class Node():
    def _init_(self, data = None, nextPointer = None):
        self.data = data
        self.nextPointer = nextPointer

class queue():
    def _init_(self):
        self.queue = LinkedList()
        self.front = None
        self.rear = None
    def getFront(self):
        return self.front.data
        
    def getRear(self):
        return self.rear.data
        
    def enqueue(self, node):
        if self.front is None and self.rear is None:
            self.front = node
            self.rear = node
            self.queue.insert(node)
        else:
            self.queue.insert(node)
            self.rear = node
            
    def dequeue(self):
        nodeToReturn = self.front
        self.queue.remove(self.front)
        self.front = self.queue.root
        return nodeToReturn.data