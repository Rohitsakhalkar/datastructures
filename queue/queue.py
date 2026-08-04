from .node import Node
from typing import Any, Iterator

class Queue:

    def __init__(self)-> None:
        self._size: int = 0
        self._max: int = None #optional if you want to set max 
        self._rear: Node | None = None 
        self._front: Node | None = None

    def __len__(self)-> int:
        return self._size

    def __iter__(self)-> Iterator[Any]:
        if self._rear is None:
            raise IndexError("queue underflow")
        else:
            current = self._front
            while current:
                yield current.value
                current = current.next

    def __bool__(self):
        return self._size >= 0

    def __str__(self)-> str:
        return f"[{",".join(str(value) for value in self)}]"

    def __repr__(self)-> str:
        return f"Queue(front to bottom)->[{",".join(str(value) for value in self)}]"

    def is_empty(self)-> bool:
        return self._size <= 0

    def is_full(self)-> bool:
        return self._size == self._max

    def front(self)-> Any:
        return self._front.value

    def rear(self)-> Any:
        return self._rear.value

    def enqueue(self, value: Any)-> None:
        newNode = Node(value)
        if self._max and self._max == self._size:
            raise OverflowError("queue overflow")
        if self._front is None:
            self._front = newNode
            self._rear = newNode
            self._size += 1 
            return
        else:
            self._rear.next = newNode
            self._rear = newNode
            self._size += 1
            return

    def dequeue(self)-> Any:
        if self._size <= 0:
            raise IndexError("queue underflow")
        
        if self._rear is self._front:
            dequeuedNode = self._front
            self._front = None
            self._rear = None
            self._size -= 1
            return dequeuedNode.value
        else:
            dequeuedNode = self._front
            self._front = dequeuedNode.next
            dequeuedNode.next = None
            self._size -= 1
            return dequeuedNode.value

    def clear(self)-> None:
        self._front = None
        self._rear = None
        self._size = 0

