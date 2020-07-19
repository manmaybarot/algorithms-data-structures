
class LinkedList:
    def __init__(self):
        self.head = None
        self.isPalindrom = True

    def print_me(self):
        tmp = self.head
        ans = str(tmp.val) + '->'
        while tmp.next:
            tmp = tmp.next
            ans += str(tmp.val) + '->'
        ans += 'None'
        return ans

    def delete_node_with_val(self, x):
        t1 = self.head
        while t1.next:
            t2 = t1.next
            if t2.val == x:
                t1.next = t2.next
                break
            t1 = t2
        else:
            print('node not found')

    def insert_at_beginning(self, x):
        node = Node(x)
        node.next = self.head
        self.head = node

    def reverse_me(self):
        previous_node = None
        current_node = self.head
        next_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def is_palindrom(self, head, node):
        if not node:
            return head

        result = self.is_palindrom(head, node.next)

        if not result:
            self.isPalindrom = False
            return self.isPalindrom
        if node.val == result.val:
            return result.next or self.isPalindrom
        else:
            self.isPalindrom = False
            return self.isPalindrom


if __name__ == '__main__':

    my_linkedlist = LinkedList()

    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(2)
    Node4 = Node(1)

    my_linkedlist.head = Node1

    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4

    print(my_linkedlist.print_me())
    # my_linkedlist.delete_node_with_val(40)
    # my_linkedlist.insert_at_beginning(500)
    print(my_linkedlist.print_me())
    my_linkedlist.reverse_me()
    print(my_linkedlist.print_me())
    print(my_linkedlist.is_palindrom(
        my_linkedlist.head, my_linkedlist.head
    ))
