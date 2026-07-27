"""Floyd's tortoise and hare: detect a cycle with two pointers and O(1) space.
A slow pointer steps once, a fast pointer twice; if they ever meet, there's a loop."""
from __future__ import annotations

from linkedlist.node import Node


def has_cycle(head: Node | None) -> bool:
    """Return True if the list contains a cycle, using O(1) extra space."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next             # tortoise: one step
        fast = fast.next.next        # hare: two steps
        if slow is fast:             # they collided -> there is a cycle
            return True
    return False                     # fast ran off the end -> no cycle
