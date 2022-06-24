class Node():
    def _init_(self, data = None, leftPointer = None, rightPointer = None):
        self.data = data
        self.leftPointer = leftPointer
        self.rightPointer = rightPointer
        
class BinaryTree():
    def _init_(self):
        self.root = None
        
    def addRoot(self, newNode):
        self.root = newNode
        
    def addLeftChild(self, newNode, parentNode):
        parentNode.leftPointer = newNode

    def addRightChild(self, newNode, parentNode):
        parentNode.rightPointer = newNode
        
    def preorder(self, node):
        if(node is None):
            return
        else:
            print(node.data)
            self.preorder(node.leftPointer)
            self.preorder(node.rightPointer)
            
    def inorder(self, node):
        if(node):
            self.inorder(node.leftPointer)
            print(node.data)
            self.inorder(node.rightPointer)
            
    def postorder(self, node):
        if(node is not None):
            self.postorder(node.leftPointer)
            self.postorder(node.rightPointer)
            print(node.data)
class BST():
    def _init_(self):
        self.bst = BinaryTree()
    
    def insert(self, newNode, parentNode):
        if(self.bst.root is None):
            self.bst.root = newNode
        else:
            if(newNode.data > parentNode.data):
                self.bst.addRightChild(newNode, parentNode)
            else:
                self.bst.addLeftChild(newNode, parentNode)
    
    def printTree(self):
        self.bst.preorder(self.bst.root)