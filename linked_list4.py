class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)


dllist = DoublyLinkedList()
dllist.append("First Node")

"""
python -i linked_list4.py

dllist.head.value
dllist.tail.value                   the head and the tail should have the same value of "First Node".

dllist.append("Second Node")
dllist.head.value
dllist.tail.value                   tail should been changed to hold the value "Second Node", whereas the head remains the same.

dllist.head.next.value
dllist.tail.prev.value

dllist.head.prev.value              These commands should result in errors saying that 'NoneType' object has no attribute value. 
dllist.tail.next.value              You cannot look at the value of the prev attribute for the head, nor the next attribute for the tail, because they both point to None.


dllist.append("Third Node")
dllist.tail.value
dllist.tail.prev.value
dllist.tail.prev.prev.value
dllist.head.next.next.value

exit()
"""