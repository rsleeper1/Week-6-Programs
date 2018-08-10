#Improved Parse Tree
#Ryan Sleeper
#This program takes an expression and evaluates it by creating a binary tree.
#I only made comments to things I changed/added to the program.

import operator

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
            
    
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
            
            
            
def buildParseTree(fpexp):             #I made a few changes to the buildParseTree method in order for it to work without having
    count = 0                          #spaces inbetween each character in the string. First, I took the string and counted how
    for item in fpexp:                 #many ")" characters there are. If there were none, I asked the programmer to insert at least
        if item == ")":                #one around the entire expression.
            count = count + 1
    if count == 0:
        raise ValueError("Please put parenthesis around expression.")
    parCount = 0
    item = 0
    while parCount != count:                 #Next, I look through the string and put spaces between characters that needed
        if fpexp[item] == ")":               #spaces in the original program. It did this by taking the ordinal values and so
                parCount = parCount + 1      #the computer knew when to put a space and when to not put a space.            
        if fpexp[item] == ' ':
            fpexp = fpexp
        elif not(ord(fpexp[item])>=48 and ord(fpexp[item])<=57 and ord(fpexp[item +1])>=48 and ord(fpexp[item +1])<=57):
            fpexp = fpexp[:item +1] + " " + fpexp[item +1:]
        item = item + 1
                                              
    fplist = fpexp.split()                  #Once it got through the string it has now transformed the string without spaces
    pStack = Stack()                        #into a string with spaces and thus can run like it did previously.
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()


def main():                             #The only thing I changed in the main function was have the expression have no spaces and
    pt = buildParseTree("((10+5)*3)")   #also to evaluate the expression so the user knows that the program is still running correctly.
    answer = evaluate(pt)               #Feel free to change the expression, just make sure you put parenthesis around the expression
    print(answer)                       #once you are done.
    
main()
    