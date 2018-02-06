# coding = utf-8


class Node(object):
    """
    Represents a singly linked node.
    """
    def __init__(self, data, next=None):
        """
        Instantiates a Node with a default next of None.
        """
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous


def test_node():
    """
    Adde five nodes t the beginning of the linked structure
    :return:
    """
    head = None
    for count in range(1, 6):
        head = Node(count, head)
    # Print the contents of the structure
    while head != None:
        print head.data
        head = head.next


def test_two_way_node():
    # Create a doubly linked structure with one node
    head = TwoWayNode(1)
    tail = head
    # Add four nodes to the end of the doubly linked structure
    for data in range(2, 6):
        tail.next = TwoWayNode(data, tail)
        tail = tail.next
    # Print the contents of the linked structure in reverse order
    probe = tail
    while probe != None:
        print probe.data
        probe = probe.previous


if __name__ == '__main__':
    test_node()
    test_two_way_node()
