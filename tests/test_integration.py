"""The techniques compose and agree with a brute-force oracle over many inputs."""
from linkedlist.singly import from_list, to_list
from linkedlist.reverse import reverse
from linkedlist.runner import middle
from linkedlist.palindrome import is_palindrome


def test_reverse_matches_python():
    for data in [[], [1], [1, 2], [1, 2, 3, 4, 5]]:
        assert to_list(reverse(from_list(data))) == data[::-1]


def test_middle_matches_index():
    for data in [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]:
        head = from_list(data)
        assert middle(head).value == data[len(data) // 2]


def test_palindrome_matches_oracle():
    for data in [[], [1], [1, 1], [1, 2], [1, 2, 1], [1, 2, 2, 1], [1, 2, 3]]:
        assert is_palindrome(from_list(data)) == (data == data[::-1])
