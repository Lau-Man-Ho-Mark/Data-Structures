class Node():
    def _init_(self, data = None, nextPointer = None):
        self.data = data
        self.nextPointer = nextPointer

class LinkedList():
    def _init_(self):
        self.root = None
    
    def insertAfter(self, newNode, target):
        currentNode = self.root
        while True:
            if(currentNode == target):
                temp = currentNode.nextPointer
                currentNode.nextPointer = newNode
                newNode.nextPointer = temp
                break

            currentNode = currentNode.nextPointer
            
    def insertBefore(self, newNode, target):
        currentNode = self.root
        if(target == self.root):
            self.root = newNode
            self.root.nextPointer = currentNode
            return
        while True:
            if(currentNode.nextPointer == target):
                temp = currentNode.nextPointer
                currentNode.nextPointer = newNode
                currentNode = currentNode.nextPointer
                currentNode.nextPointer = temp
                break

            currentNode = currentNode.nextPointer
        
    def remove(self, target):
        currentNode = self.root
        if self.root == target:
            self.root = currentNode.nextPointer
            return
        while True:
            if(currentNode.nextPointer == target):
                temp = currentNode
                temp = temp.nextPointer
                currentNode.nextPointer = temp.nextPointer
                break
                
            currentNode = currentNode.nextPointer
        
    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            currentNode = self.root
            while True:
                if(currentNode.nextPointer is None):
                    currentNode.nextPointer = node
                    break
                else:
                    currentNode = currentNode.nextPointer
    
    def printNode(self):
        currentNode = self.root
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextPointer