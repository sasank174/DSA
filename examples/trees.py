class root:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def push(self,data):
        if self.root == None:
            self.root = root(data)
        else:
            self.push_node(data,self.root)

    def push_node(self,data,node):
        if data < node.data:
            if node.left == None:node.left = root(data)
            else:self.push_node(data,node.left)
        else:
            if node.right == None:node.right = root(data)
            else:self.push_node(data,node.right)
    
    def inorder(self,node):
        if node != None:
            self.inorder(node.left)
            print(node.data,end=' ')
            self.inorder(node.right)
    
    def preorder(self,node):
        if node != None:
            print(node.data,end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self,node):
        if node != None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=' ')


n = [5,8,9,4,6]
t = Tree()
for i in n:t.push(i)
t.inorder(t.root)
print()
t.preorder(t.root)
print()
t.postorder(t.root)
