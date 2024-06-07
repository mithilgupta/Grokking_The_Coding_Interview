
# Create a Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Create a LinkedList Class 
class LinkedList:
    def __init__(self):
        self.head = None

    # insert at beginning:
    def push(self, val):
        temp_node = Node(val)

        if self.head is None:
            temp_node.next = None
            self.head = temp_node
        else:
            temp_node.next = self.head
            self.head = temp_node

    # Display the entire LL
    def show(self):
        temp_node = self.head

        while temp_node is not None:
            print(temp_node.data)
            temp_node = temp_node.next

    

    # insert at the end
    def append(self, value):
        temp_node = Node(value)

        temp_node2 = self.head

        while temp_node2.next is not None:
            # print(temp_node2.data)
            temp_node2 = temp_node2.next
            # print(temp_node2.data)

        temp_node2.next = temp_node
        temp_node.next = None


    # insert at index
    def insert(self, val, idx):
        temp_node = Node(val)

        node = self.head

        if idx == 0:
            # how do I call def push(self, val): here??
            # ll.push(val)
            pass


        for i in range(idx-1):
            node = node.next

        temp_node.next = node.next
        node.next = temp_node


    # Delete at index
    def delete(self,idx):

        temp_node = Node(0)

        if idx == 0:
            self.head = self.head.next

        else:
            node= self.head

            for i in range(idx-1):
                node = node.next

            # Catching the element to be deleted via a temp node
            temp_node.next = node.next

            # Jumping over the element to be deleted
            if node.next.next is not None:
                node.next= node.next.next
            else:
                node.next = None

            # Freeing up space
            temp_node.next = None   # Ye phat raha hai. Is this s Pass be Reference / Pass by Value issue??



    # # Reverse a linkedList
    # def reverse(self):
    #     node = self.head

    #     temp_node = Node(None)

    #     while node.next is not None:
    #         temp_node.next = node
            
    #         node = node.next

            
            

    #     # print(node.data)
    #     self.head = node
