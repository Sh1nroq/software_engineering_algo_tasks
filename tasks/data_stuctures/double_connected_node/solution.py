class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    current = node
    new_head = None

    while current:
        current.prev, current.next = current.next, current.prev

        new_head = current

        current = current.prev

    return new_head