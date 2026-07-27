from linkedlist.node import Node
from linkedlist.singly import from_list
from linkedlist.cycle import has_cycle


def test_no_cycle():
    assert has_cycle(from_list([1, 2, 3, 4])) is False


def test_no_cycle_empty():
    assert has_cycle(None) is False


def test_cycle_two_nodes():
    a, b = Node(1), Node(2)
    a.next = b
    b.next = a                       # b points back to a -> cycle
    assert has_cycle(a) is True


def test_cycle_tail_to_middle():
    a, b, c, d = Node(1), Node(2), Node(3), Node(4)
    a.next, b.next, c.next = b, c, d
    d.next = b                       # tail loops back to the second node
    assert has_cycle(a) is True
