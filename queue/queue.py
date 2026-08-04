from .node import Node
from typing import Any, Iterator

class Queue:

    def __init__(self)-> None:
        self._size: int = 0
        self._max: int = None #optional if you want to set max 
        self._rear: Node | None = None 
        self._front: Node | None = None

    def __len__(self)-> int:
        """
        Returns the length of the queue
        """
        return self._size

    def __iter__(self)-> Iterator[Any]:
        """
        Iterates over the queue fromn front to rear
        Raise:
            IndexError:
                queue underflow
        Yield:
             returns the value of the node 
        """
        if self._rear is None:
            raise IndexError("queue underflow")
        else:
            current = self._front
            while current:
                yield current.value
                current = current.next

    def __bool__(self):
        """
        Returns true if there is an element present in queue
                            or 
        Returns false if there is no element present 
        """
        return self._size >= 0

    def __str__(self)-> str:
        """
        Returns a string containting values of queue from front to rear
        """
        return f"[{",".join(str(value) for value in self)}]"

    def __repr__(self)-> str:
        """
        Returns a string containing values of queue from front to rear
        """
        return f"Queue(front to bottom)->[{",".join(str(value) for value in self)}]"

    def is_empty(self)-> bool:
        """
        Returns a true if queue is empty
                     or
        Returns false

        """
        return self._size <= 0

    def is_full(self)-> bool:
        """
        Returns true if queue is full only if you define _max
                            or
        Returns false 
        note: only works if you define _max 
        """
        return self._size == self._max

    def front(self)-> Any:
        """
        Returns the front value of the queue
        """
        return self._front.value

    def rear(self)-> Any:
        """
        Returns the rear value of the queue
        """
        return self._rear.value

    def enqueue(self, value: Any)-> None:
        """
        appends a value to the queue from the rear
        Args...
            value-> the value to be added
        Raises...
            OverflowError:
                queue overflow (only if you define _max) 
         
        """
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
        """
        removes a value from the from of the queue
        Raises...
            IndexError:
                queue underflow
        returns the value that was removed/dequeued 
        """
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
        """
        clears all the nodes of the queue
        """
        self._front = None
        self._rear = None
        self._size = 0

