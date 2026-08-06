from __future__ import annotations
from typing import Any 



class Node:
    def __init__(self, 
                 value: Any, 
                 left: Node | None = None,
                 right: Node | None = None
                 )-> None:
        self.value = value
        self.left = left
        self.right = right