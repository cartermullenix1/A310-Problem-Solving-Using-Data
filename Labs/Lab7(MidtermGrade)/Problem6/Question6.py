from BstNode import BstNode

def largestValue(bst):
    if bst.right == None:
        return bst.key
    else:
        return largestValue(bst.right)

class BST(BstNode):
    def __init__(self, name):
        super().__init__(name)

    def insert(self, value):
        if self.key == value:
            return
        elif self.key < value:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
    
    def find(self, value):
        if value == self.key:
            return True
        elif value > self.key:
            if self.right == None:
                return False
            else:
                return self.right.find(value)
        else:
            if self.left == None:
                return False
            else:
                return self.left.find(value)
    
    def remove(self,value):
        if self.key == value:
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right
            else:
                temp = largestValue(self.left)
                self.key = temp
                self.left = self.left.remove(temp)
        elif self.key < value:
            self.right = self.right.remove(value)
        else:
            self.left = self.left.remove(value)
        return self


a = BST(8)
for num in [1, 9, 7, 2, 6, 4, 5]:
    a.insert(num)
print("Consider this tree:")
a.display()
print("If I remove the root:")
a = a.remove(8)
a.display()