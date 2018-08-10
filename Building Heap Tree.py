#Build Heap Method
#Ryan Sleeper

import random 

class BinaryHeapTree:
    def __init__(self):
        self.size = 0
        self.heapList = [0]
        
    def insertNode(self, node):
        self.heapList.append(node)
        self.size = self.size + 1
        self.moveUp(self.size)
        
    def moveUp(self, node):
        while node // 2 > 0:
          if self.heapList[node] < self.heapList[node // 2]:
             self.heapList[node // 2], self.heapList[node] = self.heapList[node], self.heapList[node // 2]
          node = node // 2
          
    def moveDown(self, node):
        while (node * 2) <= self.size:
            smallestNode = self.minChild(node)
            if self.heapList[node] > self.heapList[smallestNode]:
                self.heapList[node], self.heapList[smallestNode] = self.heapList[smallestNode], self.heapList[node]
            node = smallestNode

    def minChild(self, node):
        if node * 2 + 1 > self.size:
            return node * 2
        else:
            if self.heapList[node * 2] < self.heapList[node * 2 + 1]:
                return node * 2
            else:
                return node * 2 + 1
            
    def buildHeap(self, list):
        level = len(list) // 2
        self.size = len(list)
        self.heapList = [0] + list[:]
        while (level > 0):
            self.moveDown(level)
            level = level - 1

    
def main():
    randomNumberList = random.sample(range(100), 20)
    print(randomNumberList)
    myHeapTree = BinaryHeapTree()
    myHeapTree.buildHeap(randomNumberList)
    print(myHeapTree.heapList)
        
    
main()