from linkedlist.singly import from_list, to_list
from linkedlist.reverse import reverse


def test_reverse():
    assert to_list(reverse(from_list([1, 2, 3, 4]))) == [4, 3, 2, 1]


def test_reverse_single():
    assert to_list(reverse(from_list([7]))) == [7]


def test_reverse_empty():
    assert reverse(None) is None
