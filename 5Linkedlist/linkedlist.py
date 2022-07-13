from requests import delete


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        t = node(data)
        t.next = self.head
        self.head = t

    def insert(self,data):
        t = node(data)
        if self.head == None:
            self.head = t
            return
        t1 = self.head
        while t1.next:t1 = t1.next
        t1.next = t
    
    def pop(self):
        t = self.head
        if t == None:
            return
        while t.next.next:
            t = t.next
        x = t.next
        t.next = None
        y = x.data
        del x
        return y

    
    def printlist(self):
        t = self.head
        if t == None:
            print("Empty list")
            return
        while t.next:
            print(t.data, end=" ")
            t = t.next
        print(t.data)
    
    def length(self):
        t = self.head
        c = 0
        while t:
            c += 1
            t = t.next
        return c

    def search(self,data):
        t,i = self.head,0
        while t:
            if t.data == data:return i
            t,i = t.next,i+1
    
    def delete(self,data):
        t = self.head
        if t.data == data:
            self.head = t.next
            del t
            return
        while t.next:
            if t.next.data == data:
                t.next = t.next.next
                x = t.next
                del x
                return "deleted"
            t = t.next
        print("Not found")

    def reverse(self):
        t = self.head
        if t == None:return
        prev = None
        while t:
            next = t.next
            t.next = prev
            prev = t
            t = next
        self.head = prev
    
    def merge(self,l2):
        t = self.head
        p = l2.head
        if t == None:
            self.head = p
            return
        while t.next and p:
            x,y = t.next.data,p.data
            if x > y:
                j = p
                p = p.next
                j.next = t.next
                t.next = j
            else:t = t.next



a = [1,5,7,10]
b = [2,3,6]
l1 = linkedlist()
l2 = linkedlist()
for i in a:l1.insert(i)
for i in b:l2.insert(i)
l1.printlist()
l2.printlist()
l1.merge(l2)
l1.printlist()

# l.printlist()
# print("pop:",l.pop())
# l.printlist()
# print("length:",l.length())
# print("search:",l.search(5))
# print("delete:",l.delete(5))
# l.printlist()
# l.reverse()
# l.printlist()