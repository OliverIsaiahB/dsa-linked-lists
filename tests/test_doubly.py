from linkedlist.doubly import DoublyLinkedList


def test_append():
    dll = DoublyLinkedList()
    for v in [1, 2, 3]:
        dll.append(v)
    assert dll.to_list() == [1, 2, 3]


def test_delete_middle():
    dll = DoublyLinkedList()
    nodes = [dll.append(v) for v in [1, 2, 3]]
    dll.delete(nodes[1])
    assert dll.to_list() == [1, 3]


def test_delete_head_and_tail():
    dll = DoublyLinkedList()
    nodes = [dll.append(v) for v in [1, 2, 3]]
    dll.delete(nodes[0])
    dll.delete(nodes[2])
    assert dll.to_list() == [2]


def test_delete_to_empty():
    dll = DoublyLinkedList()
    node = dll.append(5)
    dll.delete(node)
    assert dll.to_list() == []
