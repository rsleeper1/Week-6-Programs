#Binary Heap Tree
#Ryan Sleeper
#This program generates a random list of integers and then produces a heap tree by adding
#the numbers to the tree one at a time and sorting them as we append.

import random 

class BinaryHeapTree:             #This class creates a heap tree given a list of numbers.
    def __init__(self):
        self.size = 0
        self.heapList = [0]
        
    def insertNode(self, node):      #This method inserts a new node into the tree and then calls the moveUp 
        self.heapList.append(node)   #method to sort it through out the tree.
        self.size = self.size + 1
        self.moveUp(self.size)
        
    def moveUp(self, node):          #This method sorts the tree as each number gets added to it.
        while node // 2 > 0:
          if self.heapList[node] < self.heapList[node // 2]:
             self.heapList[node // 2], self.heapList[node] = self.heapList[node], self.heapList[node // 2]
          node = node // 2
          
    
def main():                                             #The main function generates a random list of numbers and then creates a 
    randomNumberList = random.sample(range(100), 20)    #heap tree and adds the numbers from the list to the heap tree one at a time.
    print(randomNumberList)                             #I have the program print out each iteration so the user can see how the tree
    myHeapTree = BinaryHeapTree()                       #is created.
    for number in range(len(randomNumberList)):
        myHeapTree.insertNode(randomNumberList[number])
        print(myHeapTree.heapList)
        
    
main()
    
        
    