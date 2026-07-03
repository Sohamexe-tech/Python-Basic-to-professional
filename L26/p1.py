#wamdoopp fro Tree: BST
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right =  None
    def add(self, ele):
        if ele < self.data:
            if self.left == None:
                self.left = Tree(ele)
            else:
                self.left.add(ele)
        else:
            if self.right == None:
                self.right = Tree(ele)
            else:
                self.right.add(ele)
    
    def show(self):
        if self.left != None:
            self.left.show()
        print(self.data,end=" ")
        if self.right != None:
            self.right.show()

root = None

while True:
    op = int(input("1 Enter 2 Show 3 Exit \n Enter your Choice: "))
    if op == 1:
        ele = int(input("Enter Element: "))
        if root == None:
            root = Tree(ele)
        else:
            root.add(ele)
    elif op == 2:
        if root == None:
            print("Tree is Empty")
        else:
            root.show()
            print()
    elif op == 3:
        break
    else:
        print("Invalid Option")
