# Reverse the Singly linked list
# Implementation of Singly LL

from LinkedList_Problems.SLL_Problems.SLLNode import SLLNode


class ReverseSLL(object):
    def __init__(self):
        self.root = None

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

    def reverse_ll_iter(self):
        prev = None
        curr = self.root
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.root = prev

    # Pending need to be complete
    def reverse_ll_rec(self, node):

        if node is None:
            return
        start = node
        rest = start.next

        if rest is None:
            return
        self.reverse_ll_rec(rest)
        start.next.next = start
        n_node = start.next
        start.next = None
        start.next = n_node
        self.root = start

    def reverse_rec(self):
        self.reverse_ll_rec(self.root)

    def print_ll(self):
        temp = self.root
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == '__main__':
    reverseSLL = ReverseSLL()
    new_node = SLLNode(45)

    # Insert the node at beginning
    reverseSLL.insert_at_begin(new_node)

    reverseSLL.insert_at_end(SLLNode(23))
    reverseSLL.insert_at_end(SLLNode(12))
    reverseSLL.insert_at_end(SLLNode(67))
    reverseSLL.insert_at_end(SLLNode(55))

    reverseSLL.print_ll()
    reverseSLL.reverse_ll_iter()
    reverseSLL.print_ll()

    reverseSLL.reverse_rec()
    reverseSLL.print_ll()
