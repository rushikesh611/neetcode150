# print linkedlist
class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
def print_list(head):
    node = head
    while node != None:
        print(node.data)
        node = node.next
# insert at end 
class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
    def Insert(head, data):
        node = head
        if head is None:
            head = Node(data)
            return head
        
        while  node.next != None:
            node = node.next
        
        node.next = Node(data)
        
        return head

# insert at head position
class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Insert(head, data):
    if head is None:
        head = Node(data)
        return head
    else:
        buf = head
        
        head = Node(data)
        head.next = buf
        
        return head

# delete node at a given position
class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Delete(head, position):
    if position == 0:
        head = head.next
    else:
        node = head
        for _ in range(position-1):
            node = node.next
        
        node.next = node.next.next
        
    return head



    
# ................................................................
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# O(1) time | O(1) space 
def setHead(self,node):
    if self.head is None:
        self.head = node
        self.tail = node
        return 
    self.insertBefore(self.head, node)

# O(1) time | O(1) space 
def setTail(self,node):
    if self.tail is None:
        self.setHead(node)
        return 
    self.insertAfter(self.tail, node)

# O(1) time | O(1) space 
def insertBefore(self,node, nodeToInsert):
    if nodeToInsert == self.head and nodeToInsert == self.tail:
        return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node.prev
    nodeToInsert.next = node
    if node.prev is None:
        self.head = nodeToInsert
    else:
        node.prev.next = nodeToInsert
    node.prev = nodeToInsert 

# O(1) time | O(1) space 
def insertAfter(self,node, nodeToInsert):
    if nodeToInsert == self.head and nodeToInsert == self.tail:
        return
    self.remove(nodeToInsert)
    nodeToInsert.prev = node
    nodeToInsert.next = node.next
    if node.next is None:
        self.tail = nodeToInsert
    else:
        node.next.prev = nodeToInsert
    node.next = nodeToInsert

# O(p) time | O(1) space where p is position
def insertAtPosition(self, position, nodeToInsert):
    if position == 1:
        self.setHead(nodeToInsert)
        return
    node = self.head
    currentPosition = 1
    while node is not None and currentPosition != position:
        node = node.next
        currentPosition += 1 
    if node is not None:
        self.insertBefore(node, nodeToInsert)
    else:
        setTail(nodeToInsert)

# O(n) time | O(1) space 
def removeNodeWithValue(self,value):
    node = self.head
    while node is not None:
        nodeToRemove = node
        node = node.next
        if nodeToRemove.value == value:
            self.remove(nodeToRemove)

# O(1) time | O(1) space 
def remove(self,node):
    if node == self.head:
        self.head = self.head.next
    if node == self.tail:
        self.tail = self.tail.prev
    self.removeNodeBindings(node)

# search method O(n) time | O(1) space 
def containsNodeWithValue(self,value):
    node = self.head
    while node is not None and node.value != value:
        node = node.next
    return node is not None

def removeNodeBindings(self,node):
    if node.prev is not None:
        node.prev.next = node.next
    node.prev = None
    if node.next is not None:
        node.next.prev = node.prev
    node.prev = None
    node.next = None