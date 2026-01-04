import pytest
from tasks.data_stuctures.double_connected_node.solution import solution, DoubleConnectedNode


def build_list(values):
    if not values:
        return None
    nodes = [DoubleConnectedNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    return nodes[0]


def list_to_py(head):
    arr = []
    cur = head
    while cur:
        arr.append(cur.value)
        cur = cur.next
    return arr


def test_solution_is_callable():
    assert callable(solution)


def test_reverse_basic():
    head = build_list([1, 2, 3, 4])
    new_head = solution(head)
    assert list_to_py(new_head) == [4, 3, 2, 1]


def test_reverse_single():
    head = DoubleConnectedNode(42)
    new_head = solution(head)
    assert new_head.value == 42
    assert new_head.next is None
    assert new_head.prev is None


def test_reverse_two_nodes():
    head = build_list(["A", "B"])
    new_head = solution(head)
    assert list_to_py(new_head) == ["B", "A"]


def test_prev_links_correct():
    head = build_list([10, 20, 30])
    new_head = solution(head)
    assert new_head.value == 30
    assert new_head.next.value == 20
    assert new_head.next.prev is new_head
    assert new_head.next.next.value == 10
    assert new_head.next.next.prev.value == 20


def test_manual_links_from_task():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    new_head = solution(node0)

    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node1.next is node0
    assert node0.next is None
    assert node0.prev is node1


def test_empty_list():
    assert solution(None) is None