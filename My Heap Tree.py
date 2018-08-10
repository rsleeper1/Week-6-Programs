#Binary Heap Tree
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
          
    
def main():
    randomNumberList = random.sample(range(100), 20)
    print(randomNumberList)
    myHeapTree = BinaryHeapTree()
    for number in range(len(randomNumberList)):
        myHeapTree.insertNode(randomNumberList[number])
        print(myHeapTree.heapList)
        
    
main()
    
        
    