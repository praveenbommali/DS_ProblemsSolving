# Implementation of Singly LL

from LinkedList_Problems.SLL_Problems.SLLNode import SLLNode


class SinglyLLImpl(object):
    def __init__(self):
        self.root = None
        self.c = 0

    def insert_at_begin(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            new_node.next = self.root
            self.root = new_node

    def insert_at_end(self, new_node):
        if self.root is None:
            self.insert_at_begin(new_node)
        else:
            temp = self.root
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def insert_at_position(self, position, new_node):
        if self.root is None:
            self.insert_at_begin(new_node)
        else:
            count = 0
            temp = self.root
            while temp:
                if count == position - 1:
                    new_node.next = temp.next
                    temp.next = new_node
                    break
                else:
                    temp = temp.next
                    count += 1


    def print_ll(self):
        temp = self.root
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == '__main__':
    singlyLLImpl = SinglyLLImpl()
    new_node = SLLNode("M")

    # Insert the node at beginning
    singlyLLImpl.insert_at_begin(new_node)

    singlyLLImpl.insert_at_end(SLLNode("A"))
    singlyLLImpl.insert_at_end(SLLNode("D"))
    singlyLLImpl.insert_at_end(SLLNode("A"))
    singlyLLImpl.insert_at_end(SLLNode("M"))

    singlyLLImpl.print_ll()

