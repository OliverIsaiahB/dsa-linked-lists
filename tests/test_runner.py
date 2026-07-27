from linkedlist.singly import from_list
from linkedlist.runner import middle


def test_middle_odd():
    # 1 2 3 4 5 -> middle is 3
    assert middle(from_list([1, 2, 3, 4, 5])).value == 3


def test_middle_even():
    # 1 2 3 4 -> second middle is 3
    assert middle(from_list([1, 2, 3, 4])).value == 3


def test_middle_single():
    assert middle(from_list([9])).value == 9


def test_middle_empty():
    assert middle(None) is None
