from linkedlist.singly import from_list
from linkedlist.palindrome import is_palindrome


def test_palindrome_odd():
    assert is_palindrome(from_list([1, 2, 3, 2, 1])) is True


def test_palindrome_even():
    assert is_palindrome(from_list([1, 2, 2, 1])) is True


def test_not_palindrome():
    assert is_palindrome(from_list([1, 2, 3])) is False


def test_palindrome_single():
    assert is_palindrome(from_list([7])) is True


def test_palindrome_empty():
    assert is_palindrome(None) is True
