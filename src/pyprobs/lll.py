class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node

    def __repr__(self):
        return f"Node(data={self.data}, next={self.next})"



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


