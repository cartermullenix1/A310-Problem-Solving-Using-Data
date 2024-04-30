def largestIn(BinaryTree):
    if BinaryTree.right == None:
        return BinaryTree.value
    else:
        return largestIn(BinaryTree.right)

class BinaryTree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def show(self):
        if self.left == None:
            left = " . "
        else:
            left = self.left.show()
        
        if self.right == None:
            right = " . "
        else:
            right = self.right.show()
        return "(" + str(self.value) +  " " + left + " " + right + ")"
    
    def insert(self, value):
        if self.right == " . " or self.right == None:
            return value
        elif self.left == " . " or self.left == None:
            return value
        elif self.value > value:
            return BinaryTree(self.value, self.left.insert(value), self.right)
        elif self.value < value:
            return BinaryTree(self.value, self.left, self.right.insert(value))
                
    
    def remove(self, value):
        if self.value == value:
            if self.left == None:
                return self.right
            else:
                a = largestIn(self.left)
                return BinaryTree(a, self.left.remove(a), self.right)
        elif self.value > value:
            return BinaryTree(self.value, self.left.remove(value), self.right)
        else:
            return BinaryTree(self.value, self.left, self.right.remove(value))
    


print("--------------------Test Cases-----------------------")

a = BinaryTree(3, None, None)
a.right = BinaryTree(5, None, None)
a.right.left = BinaryTree(4, None, None)
print(a.show()) # (3 . (5 (4 . .) .))
b = a.insert(1)
print("Insert 1 the tree becomes: " + b.show())

# a = BinaryTree(3, None, None)
# a.right = BinaryTree(5, None, None)
# a.right.left = BinaryTree(4, None, None)
# print(a.show()) # (3 . (5 (4 . .) .))
# b = a.remove(5)
# print("Remove 5 the tree becomes: " + b.show())
