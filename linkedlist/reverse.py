"""The quintessential pointer-surgery question: reverse a singly linked list in
place. Three pointers leapfrog down the list, flipping each link backward."""
from __future__ import annotations

from linkedlist.node import Node


def reverse(head: Node | None) -> Node | None:
    """Reverse the list iteratively in O(1) extra space.
    prev trails behind; nxt saves the link before we overwrite it."""
    prev: Node | None = None
    while head is not None:
        nxt = head.next          # 1. SAVE the next node before we lose it
        head.next = prev         # 2. FLIP this link to point backward
        prev = head              # 3. ADVANCE prev to the current node
        head = nxt               #    ADVANCE head to the saved next node
    return prev                  # prev is the old tail — the new head
