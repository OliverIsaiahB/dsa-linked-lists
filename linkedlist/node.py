"""A linked list is made of nodes. Each node holds a value and a reference (a
"pointer") to the next node. The list is just the first node — the head."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next: "Node | None" = None       # reference to the next node, or None at the end
