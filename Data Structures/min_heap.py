class minHeap():
    def _init_(self, size = 5):
        self.heap = [0]*size;
        self.lastIndex = 0;
        self.size = size;
    
    #Bunch of helper methods for the operations
    def getParentIndex(self, index):
        return (index - 1)//2;
        
    def getLeftChildIndex(self, index):
        return (2*index) + 1;
        
    def getRightChildIndex(self, index):
        return (2*index) + 2;
        
    def insert(self, value):
        if(self.lastIndex == self.size):
            #The size reaches the maximum
            return "Cannot insert anymore";
        else:
            self.heap[self.lastIndex] = value;
            self.checkForViolation(self.lastIndex);
            self.lastIndex+=1;
            
    def checkForViolation(self, index):
        while(self.heap[index] < self.heap[self.getParentIndex(index)]):
            self.swap(index, self.getParentIndex(index));
            index = self.getParentIndex(index);
            
    def swap(self, index, parentIndex):
        temp = self.heap[index];
        self.heap[index] = self.heap[parentIndex];
        self.heap[parentIndex] = temp;
        
    def printNodes(self):
        for data in self.heap:
            print(data);
            
    def deleteMin(self):
        self.heap[0] = self.heap[self.lastIndex];
        self.shiftSmallerChild(0);
        
    def hasLeftChild(self, index):
        return ((2*index) + 1) < self.lastIndex;
        
    def hasRightChild(self, index):
        return ((2*index) + 2) < self.lastIndex;
        
    def shiftSmallerChild(self, index):
        if(not self.hasLeftChild(index) and not self.hasRightChild(index)):
            self.heap[index] = 0;
            self.lastIndex-=1;
            return;
        if(not self.hasLeftChild(index) and self.hasRightChild(index)):
            self.swap(index, self.getRightChildIndex(index));
            
        if(self.hasLeftChild(index) and not self.hasRightChild(index)):
            self.swap(index, self.getLeftChildIndex(index));
        
        if(self.hasLeftChild(index) and self.hasRightChild(index)):
            left = self.heap[self.getLeftChildIndex(index)];
            right = self.heap[self.getRightChildIndex(index)];
            if(left < right):
            #Shift left up
                self.swap(index, self.getLeftChildIndex(index));
                self.shiftSmallerChild(self.getLeftChildIndex(index));
            else:
            #Shift right up
                self.swap(index, self.getRightChildIndex(index));
                self.shiftSmallerChild(self.getRightChildIndex(index));