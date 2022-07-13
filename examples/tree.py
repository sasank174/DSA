class root:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None
		# self.root = root(1)
		# self.root.left = root(2)
		# self.root.right = root(3)
		# self.root.left.left = root(4)
		# self.root.left.right = root(5)
		# self.root.right.left = root(6)
		# self.root.right.right = root(7)
	
	def insert(self,data):
		if self.root == None:
			self.root = root(data)
		else:
			self.insert_node(data,self.root)
	
	def insert_node(self,data,node):
		if data < node.data:
			if node.left == None:node.left = root(data)
			else:self.insert_node(data,node.left)
		else:
			if node.right == None:node.right = root(data)
			else:self.insert_node(data,node.right)

	def inorder(self):
		if self.root!=None:
			self.inorder_node(self.root)
			print()
	def inorder_node(self,node):
		if node!=None:
			self.inorder_node(node.left)
			print(node.data,end=' ')
			self.inorder_node(node.right)
	
	def preorder(self):
		if self.root!=None:
			self.preorder_node(self.root)
			print()
	def preorder_node(self,node):
		if node!=None:
			print(node.data,end=' ')
			self.preorder_node(node.left)
			self.preorder_node(node.right)
	
	def postorder(self):
		if self.root!=None:
			self.postorder_node(self.root)
			print()
	def postorder_node(self,node):
		if node!=None:
			self.postorder_node(node.left)
			self.postorder_node(node.right)
			print(node.data,end=' ')

n = [1,2,3,4,5,6,7]
n = [3,5,6,7,1,4,2]
o = Tree()
for i in n:o.insert(i)
print("Inorder: ",end=' ')
o.inorder()
print("Preorder: ",end=' ')
o.preorder()
print("Postorder: ",end=' ')
o.postorder()