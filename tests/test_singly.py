from linkedlist.singly import from_list, to_list, prepend, delete_value


def test_round_trip():
    assert to_list(from_list([1, 2, 3])) == [1, 2, 3]


def test_empty():
    assert from_list([]) is None
    assert to_list(None) == []


def test_single():
    assert to_list(from_list([42])) == [42]


def test_prepend():
    head = prepend(from_list([2, 3]), 1)
    assert to_list(head) == [1, 2, 3]


def test_delete_middle():
    head = delete_value(from_list([1, 2, 3]), 2)
    assert to_list(head) == [1, 3]


def test_delete_head():
    head = delete_value(from_list([1, 2, 3]), 1)
    assert to_list(head) == [2, 3]


def test_delete_absent():
    head = delete_value(from_list([1, 2, 3]), 99)
    assert to_list(head) == [1, 2, 3]
