class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data:int):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node

    def __repr__(self):
        return f"Node(data={self.data}, next={self.next})"

class LinkedList:
    def __init__(self):
        self.head = None
        self._count = 0

    def insert(self, value:int):
        """
        Will add in ascending order
        """

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self._count += 1
            return self._count

        curr_node = self.head
        prev_node = None

        while curr_node is not None:
            # check if new data is less than current data
            if new_node.get_data() < curr_node.get_data():
                # TRUE: set new node's next to current node
                new_node.set_next(curr_node)

                # check if prev node is None
                if prev_node is None:
                    # TRUE: we need to update head
                    self.head = new_node
                else:
                    # FALSE: set previous node's next to new node
                    prev_node.set_next(new_node)

                # udpdate count and return
                self._count += 1
                return self._count

            # Iterate through list
            prev_node = curr_node
            curr_node = curr_node.get_next()

        # if we have reached the end of list then current node will be None
        if curr_node is None:
            # we need to add new node to the end
            prev_node.set_next(new_node)

        self._count += 1

        return self._count

    def insert_at_head(self, value:int):
        """
        Will add new data to the beginning of the list
        """

        new_node = Node(value)
        new_node.set_next(self.head)

        self.head = new_node
        self._count += 1

        return self._count

    def get_length(self):
        return self._count

    def display(self):
        if self.head is None:
            print("List is currently empty.")
            return 0

        curr_node = self.head
        counter = 0

        while curr_node is not None:
            print(curr_node.get_data(), " -> ")
            curr_node = curr_node.get_next()
            counter += 1

        print("NULL")
        return counter



MAIN = __name__ == "__main__"

if MAIN:
    a_node = Node(1)
    b_node = Node(3)

    print(f"{a_node=}\t{a_node.get_next()}\n{b_node=}\t{b_node.get_next()}")
    print("Setting a_node's next to b_node")

    a_node.set_next(b_node)
    print(f"{a_node=}")

    print(f"Setting new value for b_node")

    b_node.set_data(2)
    print(f"{a_node=}")

    print("Creating new linked list.")

    a_list = LinkedList()

    a_list.display()

    print("Inserting at head value 5, 3, and 1.")

    a_list.insert_at_head(5)
    a_list.insert_at_head(3)
    a_list.insert_at_head(1)
    a_list.display()
    print(f"Length of a_list is {a_list.get_length()}")

    print("Now inserting (asc) 4, 2, 6, and 0.")
    a_list.insert(4)
    a_list.insert(2)
    a_list.insert(6)
    a_list.insert(0)
    a_list.display()
    print(f"Length of a_list is {a_list.get_length()}")

    print("Finished")





