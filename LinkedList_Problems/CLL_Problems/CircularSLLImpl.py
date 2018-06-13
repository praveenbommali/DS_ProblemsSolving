# Implementation of Circular Singly Linked List
from LinkedList_Problems.CLL_Problems.CSLLNode import CSLLNode


class CircularSLLImpl(object):
    def __init__(self):
        self.head = None
        self.head1 = None
        self.head2 = None

    def insert_at_begin(self, new_node):
        new_node.next = self.head
        temp = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node

        self.head = new_node

    def insert_at_end(self, new_node):
        if self.head is None:
            self.insert_at_begin(new_node)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def insert_at_position(self, position, new_node):
        count = 0
        temp = self.head

        while temp.next != self.head:

            if count == position - 1:
                break
            count += 1
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_end(self):
        if self.head is None:
            return
        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = temp.next
        del temp

    def delete_at_begin(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        del_node = self.head
        temp.next = self.head.next
        self.head = self.head.next
        del del_node

    def divide_half_cll(self, head1, head2):
        m_node, n_node = self.find_middle()

        if n_node.next.next == self.head:
            n_node = n_node.next

        # cycle1 head
        head1.head = self.head
        # cycle2 head
        if self.head.next != self.head:
            head2.head = m_node.next

        # loop the cycle2
        n_node.next = m_node.next
        n_node.next = self.head
        # loop the cycle1
        m_node.next = self.head
        return head1, head2

    def find_middle(self):
        temp = self.head
        m_node = self.head
        n_node = self.head

        while n_node.next != self.head and n_node.next.next != self.head:
            m_node = m_node.next
            n_node = n_node.next.next

        return m_node, n_node

    def print_ll(self):
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("\n")

    def print_cycle(self, node):
        print(" ::Cycle print:: ")
        temp = node.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("\n")


if __name__ == '__main__':
    circularSLLImpl = CircularSLLImpl()
    circularSLLImpl.insert_at_begin(CSLLNode(20))
    circularSLLImpl.insert_at_begin(CSLLNode(25))
    circularSLLImpl.insert_at_begin(CSLLNode(30))
    circularSLLImpl.insert_at_end(CSLLNode(35))
    circularSLLImpl.insert_at_begin(CSLLNode(15))
    circularSLLImpl.insert_at_begin(CSLLNode(10))
    circularSLLImpl.insert_at_begin(CSLLNode(5))
    circularSLLImpl.insert_at_begin(CSLLNode(2))
    circularSLLImpl.insert_at_begin(CSLLNode(3))
    circularSLLImpl.insert_at_position(3, CSLLNode(28))

    circularSLLImpl.print_ll()
    circularSLLImpl.find_middle()
    head1 = CircularSLLImpl()
    head2 = CircularSLLImpl()
    head1, head2 = circularSLLImpl.divide_half_cll(head1, head2)
    circularSLLImpl.print_cycle(head1)
    circularSLLImpl.print_cycle(head2)

    circularSLLImpl.delete_at_end()
    circularSLLImpl.print_ll()
    circularSLLImpl.delete_at_begin()
    circularSLLImpl.print_ll()
