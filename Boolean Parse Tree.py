#Boolean Parse Tree
#Ryan Sleeper
#This program takes an expression or boolean and evaluates it by creating a binary tree.
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
            
            
            
def buildParseTree(fpexp):                           #I made a few changes to the buildParseTree method in order for it to work with boolean expressions.
    count = 0                                        #All of the changes I made in the Improved Parse Tree program also apply to this program.
    for item in fpexp:                               #I had to add a few more if statements since I didn't want to put spaces in between the boolean
        if item == ")":                              #symbols. Other than that nothing else changed. The program looks through the string and puts
            count = count + 1                        #spaces where needed.
    if count == 0:
        raise ValueError("Please put parenthesis around expression or boolean statement.")
    parCount = 0
    item = 0
    while parCount != count:
        if fpexp[item] == ")":
            parCount = parCount + 1
        if fpexp[item] in ["<", ">", "!", "="] and fpexp[item + 1] == "=":
            fpexp = fpexp
        elif fpexp[item] == ' ':
            fpexp = fpexp
        elif not(ord(fpexp[item])>=48 and ord(fpexp[item])<=57 and ord(fpexp[item +1])>=48 and ord(fpexp[item +1])<=57):
            fpexp = fpexp[:item +1] + " " + fpexp[item +1:]
        item = item + 1
        
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')', '<', '>', '!=', '<=', '>=', '==']:   #Here I added the boolean symbols.
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/', '<', '>', '!=', '<=', '>=', '==']:    #Once again, the boolean symbols were needed.
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
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '<':operator.lt, '>':operator.gt, '!=':operator.ne, '<=':operator.le, '>=':operator.ge, '==':operator.eq}

    leftC = parseTree.getLeftChild()             #In the evaluate function I had to add the boolean 
    rightC = parseTree.getRightChild()           #symbols to the opers variable.

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()


def main():                               #In the main function I create three parse trees all with different
    pt = buildParseTree("(10 == 5)")      #boolean expressions. Please feel free to play around with the expressions.
    pt2 = buildParseTree("(10 > 5)")      #Just be sure to put parenthesis around the expression once you are done.
    pt3 = buildParseTree("(10 <= 5)")     #I have the program print out the results to each expression so the user
    answer = evaluate(pt)                 #knows that the program is running correctly.
    answer2 = evaluate(pt2)
    answer3 = evaluate(pt3)
    print(answer)
    print(answer2)
    print(answer3)
    
main()