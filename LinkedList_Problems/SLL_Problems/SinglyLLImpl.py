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
                del del_node
            self.root = temp

    def get_size(self):
        count = 0
        if self.root is None:
            return 0
        else:
            temp = self.root
            while temp:
                count += 1
                temp = temp.next
            return count

    def get_size_rec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_size_rec(node.next)

    def get_size_r(self):
        return self.get_size_rec(self.root)

    def search_ll_itr(self, key):
        if self.root is None:
            return
        else:
            temp = self.root
            while temp:
                if temp.data == key:
                    return True
                temp = temp.next
            return False

    def search_ll_rec(self, node, key):
        if not node:
            return False
        if node.data == key:
            return True
        else:
            return self.search_ll_rec(node.next, key)

    def search_ll(self, key):
        if self.search_ll_rec(self.root, key):
            return True
        else:
            return False

    def find_nthnode(self, node_no):
        if self.root is None:
            return -1
        count = 1
        temp = self.root
        while temp.next:
            if count == node_no:
                return temp.data
            count += 1
            temp = temp.next
        return -1

    def find_nth_node_rec(self, node, no):
        count = 1
        if count == no:
            return node.data
        else:
            return self.find_nth_node_rec(node.next, no - 1)

    def get_nth_node(self, no):
        return self.find_nth_node_rec(self.root, no)

    # Iterative method to solve
    def find_nthnode_rev_iter(self, node_no):
        size_ll = self.get_size_rec(self.root)
        node_to_find = size_ll - node_no + 1
        count = 0
        temp = self.root
        while temp:
            count += 1
            if count == node_to_find:
                return temp.data

            temp = temp.next
        return -1

    def find_nthrev_rec(self, node, no):
        if not node:
            return
        self.find_nthrev_rec(node.next, no)
        self.c += 1
        if self.c == no:
            print(node.data)

    def find_nth_r(self, no):
        return self.find_nthrev_rec(self.root, no)

    # Find the nth node in reverse of linked list
    def find_nth_rev(self, no):
        main, temp = self.root, self.root
        c = 0
        while main:
            if c >= no:
                temp = temp.next
            main = main.next
            c += 1
        if temp:
            return temp.data

    def find_middle(self):
        prev_n = self.root
        next_n = self.root
        while next_n != None and next_n.next != None:
            prev_n = prev_n.next
            next_n = next_n.next.next

        return prev_n.data

    def occurrence_ll(self, node, key):
        if not node:
            return 0
        if node.data == key:
            return 1 + self.occurrence_ll(node.next, key)
        else:
            return self.occurrence_ll(node.next, key)

    def occurrence(self, key):
        return self.occurrence_ll(self.root, key)

    def detect_loop1(self):
        s = set()
        temp = self.root

        while temp:
            if temp in s:
                return True
            temp = temp.next
        return False

    def print_ll(self):
        temp = self.root
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")


if __name__ == '__main__':
    singlyLLImpl = SinglyLLImpl()
    new_node = SLLNode(20)

    # Insert the node at beginning
    singlyLLImpl.insert_at_begin(new_node)
    new_node = SLLNode(30)
    singlyLLImpl.insert_at_begin(new_node)

    # Insert the node at end
    singlyLLImpl.insert_at_end(SLLNode(40))
    singlyLLImpl.insert_at_end(SLLNode(80))
    # Insert the node at specified position
    singlyLLImpl.insert_at_position(2, SLLNode(25))
    singlyLLImpl.insert_at_position(1, SLLNode(5))
    singlyLLImpl.insert_at_position(2, SLLNode(15))
    singlyLLImpl.insert_at_position(8, SLLNode(50))
    singlyLLImpl.insert_at_end(SLLNode(90))
    singlyLLImpl.insert_at_begin(SLLNode(10))
    singlyLLImpl.insert_at_begin(SLLNode(20))
    singlyLLImpl.insert_at_end(SLLNode(70))
    singlyLLImpl.insert_at_end(SLLNode(50))
    singlyLLImpl.insert_at_end(SLLNode(50))
    singlyLLImpl.insert_at_end(SLLNode(50))
    singlyLLImpl.insert_at_end(SLLNode(50))

    singlyLLImpl.print_ll()

    # Finding the size of linked lise
    print("Size of linked list in iterative way  : ", singlyLLImpl.get_size())
    print("Size of linked list in recursive way :", singlyLLImpl.get_size_r())

    # Search the linked list
    print("Given key 40 available in LL in iterative way: ", singlyLLImpl.search_ll_itr(40))
    print("Given key 4 available in LL in  recursive  way : ", singlyLLImpl.search_ll(4))

    # Nth node in the linked list
    print("In Linked list find the 4th Node in iter: ", singlyLLImpl.find_nthnode(4))
    print("In Linked list find the 4th Node in rec : ", singlyLLImpl.get_nth_node(4))

    # Nth node in from reverse
    print("In Linked List find 4th Node in rev_iter :: Approach1", singlyLLImpl.find_nthnode_rev_iter(4))
    print("In Linked List find 4th Node in rev_rec :: Approach1 ", singlyLLImpl.find_nth_r(4))
    print("In Linked List find 4th Node in rev :: Approach2 ", singlyLLImpl.find_nth_rev(4))

    # Find the middle node in the linked list
    print("Middle Node in LL : ", singlyLLImpl.find_middle())

    # Find the occurrence of number in linked list
    print("Occurrence of 50 in linked list : ", singlyLLImpl.occurrence(50))

    # Detecting the loops in linked list
    print("Detect the loop in linked list :: Approach1(set) ", singlyLLImpl.detect_loop1())
    print("Detect the loop in linked list :: Approach2(Floyd's Cycle) ")

    # Delete Node from Linked list
    print("\n Delete nodes from linked list")
    singlyLLImpl.delete_node(SLLNode(25))
    singlyLLImpl.delete_node(SLLNode(80))
    singlyLLImpl.delete_node(SLLNode(30))
    singlyLLImpl.delete_node(SLLNode(5))
    singlyLLImpl.print_ll()

    # Delete all node
    print("\n Delete all nodes from one by one ")
    singlyLLImpl.delete()
    singlyLLImpl.print_ll()
