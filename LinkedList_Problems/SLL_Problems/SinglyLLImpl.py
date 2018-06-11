# Implementation of Singly LL

from LinkedList_Problems.SLL_Problems.SLLNode import SLLNode


class SinglyLLImpl(object):
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

    def delete_node(self, del_node):
        if del_node is None:
            print("no node to delete")
        else:
            temp = self.root
            prev = None
            while temp:
                if temp.data is del_node.data:
                    break
                prev = temp
                temp = temp.next
            if prev is None:
                self.root = temp.next
                return
            else:
                prev.next = temp.next
                return

    def delete(self):
        if self.root is None:
            return
        else:
            temp = self.root
            while temp:
                del_node = temp
                temp = temp.next
                del_node = None
            self.root = temp


    def print_ll(self):
        temp = self.root
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == '__main__':
    singlyLLImpl = SinglyLLImpl()
    new_node = SLLNode(20)

    singlyLLImpl.insert_at_begin(new_node)
    new_node = SLLNode(30)
    singlyLLImpl.insert_at_begin(new_node)
    singlyLLImpl.insert_at_end(SLLNode(40))
    singlyLLImpl.insert_at_end(SLLNode(80))
    singlyLLImpl.insert_at_position(2, SLLNode(25))
    singlyLLImpl.insert_at_position(1, SLLNode(5))
    singlyLLImpl.insert_at_position(2, SLLNode(15))
    singlyLLImpl.insert_at_position(8, SLLNode(50))
    singlyLLImpl.print_ll()
    singlyLLImpl.delete_node(SLLNode(25))
    singlyLLImpl.delete_node(SLLNode(80))
    singlyLLImpl.delete_node(SLLNode(30))
    singlyLLImpl.delete_node(SLLNode(5))
    singlyLLImpl.print_ll()
    singlyLLImpl.delete()
    singlyLLImpl.print_ll()
