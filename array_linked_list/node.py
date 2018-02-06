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


if __name__ == '__main__':
    test_node()
