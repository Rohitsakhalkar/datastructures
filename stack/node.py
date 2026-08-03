from __future__ import annotations
from typing import Any 



class Node:
    def __init__(
            self, 
            value: Any, 
            previous: Node | None = None
                )-> None:
        
        self.value = value
        self.previous = previous