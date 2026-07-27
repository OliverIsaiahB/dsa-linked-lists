"""Building and walking a singly linked list. The whole list is reachable from
the head by following next pointers until we hit None."""
from __future__ import annotations

from linkedlist.node import Node


def from_list(values: list[int]) -> Node | None:
    """Build a linked list from a Python list, preserving order.
    Build back-to-front so each new node points at the previous head."""
    head: Node | None = None
    for v in reversed(values):
        head = Node(v, head)         # new node points at the old head
    return head


def to_list(head: Node | None) -> list[int]:
    """Walk the list, collecting values — the canonical traversal."""
    out: list[int] = []
    while head is not None:          # stop at the end sentinel, None
        out.append(head.value)
        head = head.next             # step to the next node
    return out


def prepend(head: Node | None, value: int) -> Node:
    """Insert at the front in O(1): new node points at the old head."""
    return Node(value, head)


def delete_value(head: Node | None, value: int) -> Node | None:
    """Delete the FIRST node with this value; return the (possibly new) head.
    Re-point the previous node's next around the doomed node."""
    if head is None:
        return None
    if head.value == value:          # deleting the head is the special case
        return head.next
    prev = head
    while prev.next is not None:
        if prev.next.value == value:
            prev.next = prev.next.next   # skip the doomed node
            return head
        prev = prev.next
    return head                      # value not found: list unchanged
