class Node():
    def _init_(self, data = None, nextPointer = None):
        self.data = data
        self.nextPointer = nextPointer

class stack():
    def _init_(self):
        self.stack = LinkedList()
        self.top = None
    
    def pop(self):
        nodeToReturn = self.top
        self.stack.remove(self.stack.root)
        self.top = self.stack.root
        return nodeToReturn.data
        
    def push(self, node):
        if self.top is None:
            self.stack.insert(node)
            self.top = node
        else:
            self.stack.insertBefore(node, self.top )
            self.top = node
            
    def printStack(self):
        self.stack.printNode()