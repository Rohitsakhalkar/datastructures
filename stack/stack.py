from .node import Node
from typing import Any, Iterator

class Stack:

    def __init__(self)-> None:
        self.top: Node | None = None
        self._max: int  = None #optional depends on user
        self._size: int = 0

    def __iter__(self)-> Iterator[Any]:
        """
        iterates over a stack and returns a value 
        Raises...
            IndexError:
                if stack is empty
        yield...
            return the value from stack 
        """
        if self.top is None:
            raise IndexError("Stack is Empty")
        current = self.top
        while current:
            yield current.value
            current = current.previous

    def is_empty(self)-> bool:
        """
        checks if stack is empty or not 
        returns True if empty
                or
        returns False 
        """
        if self._size == 0:
            return True
        else:
            return False

    def is_full(self)-> bool:
        """
        checks id stack is full only when you set the _max value
        returns True is Stack is equal to _max
                        or 
        returns False
        """
        if self._max and self._size == self._max:
            return True
        else:
            return False

    def __len__(self)-> int:
        """
        returns the length of the stack
        """
        return self._size

    def __str__(self)-> str:
        """
        returns a string containing the value of stack from top to bottom
        """
        return f"[{",".join(str(value) for value in self)}]"

    def __repr__(self)-> str:
        """
        returns a string containing the value of stack from top to bottom
        """
        return f"Stack(top->bottom)[{",".join(str(value) for value in self)}]"

    def push(self, value: Any)-> None:
        """
        adds a value in the stack
        Args...
            value-> the value to be added to stack
        raises...
            OverflowError:
                if _max is set and the _size equals to _max then error is raised

        """
        newNode = Node(value)
        if  self._max and self._size >= self._max:
            raise OverflowError("stack overflow")
        if not self.top:
            self.top = newNode
            self._size += 1
            return 
        else:
            current = self.top
            newNode.previous = current
            self.top = newNode
            self._size += 1
            return
        
    def pop(self)-> Any:
        """
        used to remove a value from stack from top
        Raises...
            IndexError(underFlow):
                if there are no values left in the stack to pop
        returns the value that was poped
        """
        current = self.top
        if self._size <= 0:
            raise IndexError("stack underflow")
        else:
            self.top = current.previous 
            current.previous = None
            self._size -= 1
            return current.value

    def peek(self)-> Any:
        """
        returns a value the is present at the top of the stack
        Raises...
            IndexError(underFlow):
                if stack is empty
        """
        if self._size <= 0:
            raise IndexError("stack underflow")
        else:
            return self.top.value

    def clear(self)-> None:
        """
        clears all the value from stack
         Raises...
            IndexError(underFlow):
                if stack is empty
        """
        self.top = None
        self._size = 0