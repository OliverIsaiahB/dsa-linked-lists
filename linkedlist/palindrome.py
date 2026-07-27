"""A capstone that composes two techniques you built: find the middle with the
runner, reverse the second half, then compare the halves. O(n) time, O(1) space."""
from __future__ import annotations

from linkedlist.node import Node
from linkedlist.runner import middle
from linkedlist.reverse import reverse


def is_palindrome(head: Node | None) -> bool:
    """True if the list reads the same forwards and backwards.
    Compose: middle (runner) + reverse (three-pointer) + a two-pointer compare."""
    if head is None or head.next is None:
        return True                      # empty or single node is a palindrome
    mid = middle(head)                   # runner technique finds the midpoint
    second = reverse(mid)                # reverse from the middle onward
    first = head
    while second is not None:            # compare the front half to the reversed back half
        if first.value != second.value:
            return False
        first = first.next
        second = second.next
    return True
