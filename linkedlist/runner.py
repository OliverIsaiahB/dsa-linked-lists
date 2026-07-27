"""The runner (fast/slow) technique: advance one pointer twice as fast as the
other. When the fast one reaches the end, the slow one is at the middle."""
from __future__ import annotations

from linkedlist.node import Node


def middle(head: Node | None) -> Node | None:
    """Return the middle node in ONE pass. For even length, returns the second
    of the two middle nodes (fast/slow with this loop condition)."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next             # one step
        fast = fast.next.next        # two steps — twice as fast
    return slow                      # slow is at the midpoint when fast finishes
