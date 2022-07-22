class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head == None:
            self.head = node(data)
            return
        else:
            t = self.head
            while True:
                if data < t.data:
                    if t.left == None:
                        t.left = node(data)
                        return
                    else:t = t.left
                else:
                    if t.right == None:
                        t.right = node(data)
                        return
                    else:t = t.right

    def height(self,t):
        if t == None:
            return 0
        else:
            return 1 + max(self.height(t.left), self.height(t.right))
    
    def print_tree(self,t):
        if t==None:return
        else:
            self.print_tree(t.left)
            print(t.data,end=" ")
            self.print_tree(t.right)
    
    def height_sum(self,t,s,c=0,h=0):
        if c == s:
            print("DONE",h)
            return h
        if t==None:return
        if c>s:return
        else:
            self.height_sum(t.left,s,c + t.data,h+1)
            self.height_sum(t.right,s,c + t.data,h+1)


T = tree()
a = [5,8,4,1,2,3,6,7,9,10]
for i in a:T.insert(i)
print(T.height(T.head))
T.print_tree(T.head)


#         5
#     4       8
# 1        6      9
#     2       7       10
#         3