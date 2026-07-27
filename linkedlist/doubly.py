"""A doubly linked list: each node also has a prev pointer. The extra link costs
memory but enables backward traversal and O(1) deletion of a KNOWN node."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DNode:
    value: int
    prev: "DNode | None" = None
    next: "DNode | None" = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: DNode | None = None
        self.tail: DNode | None = None

    def append(self, value: int) -> DNode:
        """Add to the back in O(1) — we keep a tail pointer."""
        node = DNode(value, prev=self.tail)
        if self.tail is not None:
            self.tail.next = node        # old tail points forward to new node
        else:
            self.head = node             # empty list: new node is also the head
        self.tail = node
        return node

    def delete(self, node: DNode) -> None:
        """Delete a KNOWN node in O(1) by re-pointing its neighbors at each other."""
        if node.prev is not None:
            node.prev.next = node.next   # left neighbor skips forward over node
        else:
            self.head = node.next        # node was the head
        if node.next is not None:
            node.next.prev = node.prev   # right neighbor skips back over node
        else:
            self.tail = node.prev        # node was the tail

    def to_list(self) -> list[int]:
        out: list[int] = []
        node = self.head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out
