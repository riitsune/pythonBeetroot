class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self, head, tail, current):
        self.head = None
        self.tail = None
        self.current = head

    def add_node_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

 #iterating without using __next__
            
     def __iter__(self):
            current = self.head
            while current:
                yield current.value
                current = current.next_node
                
                
#method to add new nodes to head

    def add_head_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            node.prev = self.head
            self.head = node



        












