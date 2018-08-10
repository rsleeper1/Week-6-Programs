#Build Heap Method
#Ryan Sleeper
#This program generates a random list of integers and then creates a heap tree
#from the numbers in the list.

import random 

class BinaryHeapTree:          #This class creates a binary heap tree given a list.
    def __init__(self):
        self.size = 0
        self.heapList = [0]
        
        
    def moveDown(self, node):                   #This method calls the minChild method and then swaps the nodes if the 
        while (node * 2) <= self.size:          #current node is greater than the smallest node. 
            smallestNode = self.minChild(node)
            if self.heapList[node] > self.heapList[smallestNode]:
                self.heapList[node], self.heapList[smallestNode] = self.heapList[smallestNode], self.heapList[node]
            node = smallestNode


    def minChild(self, node):                  #This method finds the smallest child in the tree on the current
        if node * 2 + 1 > self.size:           #level of the tree it is on and then returns it to the moveDown method.
            return node * 2
        else:
            if self.heapList[node * 2] < self.heapList[node * 2 + 1]:
                return node * 2
            else:
                return node * 2 + 1
            
            
    def buildHeap(self, list):             #This method takes a list of integers and produces a heap tree by 
        level = len(list) // 2             #first initializing the heap list and then using the moveDown method
        self.size = len(list)              #to sort the list.
        self.heapList = [0] + list[:]
        while (level > 0):
            self.moveDown(level)
            level = level - 1

    
def main():                                               #The main function generates a random list of integers and then 
    randomNumberList = random.sample(range(100), 20)      #creats a binary heap tree and prints out the results.
    print(randomNumberList)
    myHeapTree = BinaryHeapTree()
    myHeapTree.buildHeap(randomNumberList)
    print(myHeapTree.heapList)
        
    
main()