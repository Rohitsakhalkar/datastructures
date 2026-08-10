# Built by Sakhalkar, in search of meaning.
from .node import Node 
from typing import Any, Iterator



class SinglyLinkedList:
     def __init__(self):
          self._size: int = 0
          self.head: Node | None = None
          self.tail: Node | None = None
     
     def __len__(self)-> int:
          """
          returns the size of node
          """
          return self._size
     
     def __str__(self)-> str:
          """
          returns a string of values
          """
          return f"[{" , ".join(str(value)for value in self)}]"
     
     def __repr__(self)-> str:
          """
          returns a string of object info
          """
          return f"object: {self.__class__.__name__}({[ele for ele in self]})"

     def __bool__(self)-> bool:
          """
          returns true if the linked list has nodes
                         or
          returns false 
          """
          return self._size > 0
     
     def __eq__(self, other: Node)-> bool:
          """
          Args...
               other-> object of another linked list
          returns true if two object are equal or same
                         or
          returns false 
          """
          if self is other:
               return True
          if self._size == len(other):
               current = self.head
               for i in other:
                    if i != current.value:
                         return False
                    current = current.next
               return True
          return False

     def __reversed__(self)-> Iterator[Any]:
          """
          returns the reversed linked list 
          doesn't mutate values of the linked list
          Raises...
               IndexError:
                    if linked list is empty
          """
          if self.head is None:
               raise IndexError("linked list is empty")
          if self.head is self.tail:
               return self.head.value
          else:
               current = self.head
               stack = []
               while current:
                    stack.append(current.value)
                    current = current.next
          while stack:
               yield stack.pop()

     def __getitem__(self, key: int)-> Any:
          """
          Args...
               key-> integer index of the value
          returns the value from the node based on the key
          Raises...
               IndexError:
                    if linked list is empty
                              or
                    index/key is greater then the size of linked list
          """
          if self.head is None:
               raise IndexError("list is empty")
          if key < 0:
               key += self._size
          if key >= self._size or key < 0:
               raise IndexError("index out of bound")
          if key == 0:
               return self.head.value
          elif key == self._size - 1:
               return self.tail.value
          else :
               return self._get_node(key).next.value 
     
     def __setitem__(self, key: int, value: Any)-> None:
          """
          inserts a value on the existing index of  linked list 
          Args...
               key-> index where the value is to be inserted
               value-> value to be inserted
          Raises:
               IndexError:
                    if no node is present
                              or
                    key is greater then the length of linked list

          """
          newNode = Node(value)
          if self.head is None:
               raise IndexError("list is empty")
          if key < 0:
               key += self._size
          if key >= self._size or key < 0:
               raise IndexError("index out of bound")
          if self.head is self.tail:
               self.head = newNode
               self.tail = newNode
               return
          elif self.head.next is self.tail:
               if key == 0:
                    newNode.next = self.head.next
                    self.head.next = None
                    self.head = newNode
               else:
                    self.head.next = newNode
                    self.tail = newNode
               return
          elif key == 0:
               newNode.next = self.head.next
               self.head.next = None
               self.head = newNode 
               return
          elif key == self._size - 1:
               current = self._get_node(key-1)
               current.next.next = newNode
               self.tail = newNode
               return 
          else:
               current = self._get_node(key)
               newNode.next = current.next.next
               current.next = newNode
               return

     def __delitem__(self, key: int)-> None:
          """
          deletes an item of the based on the key
          Args...
               key-> index of the value to be deleted
          Raises...
               IndexError:
                    if linked list is empty
                              or
                    index is greater then size
          """
          if self.head is None:
               raise IndexError("list is empty")
          if key < 0:
               key += self._size
          if key >= self._size or key < 0:
               raise IndexError("index out of bound")
          if self.head is self.tail and key == 0:
               self.head = None
               self.tail = None
               self._size -= 1
               return
          elif self.head.next is self.tail:
               if key == 0:
                    self.head.next = None
                    self.tail = self.head
               else:
                    self.head = self.head.next
               self._size -= 1
               return
          elif key == self._size - 1:
               current = self._get_node(key-1)
               current.next.next = None
               self.tail = current.next
               self._size -= 1
               return
          elif key == 0:
               self.head = self.head.next
               self._size -= 1
               return
          else:
               current =  self._get_node(key)
               current.next = current.next.next
               self._size -= 1
               return

     def __contains__(self, value: Any)-> bool:
          """
          takes a value and check if value is present in linked list 
          Args...
               value-> takes a value
          returns True if value is present 
                         or 
          returns False
          Raises...
               IndexError:
                    if linked list is empty
          """
          if self.head is None:
               raise IndexError("list is empty")
          if self.head.value == value:
               return True
          if self.tail.value == value:
               return True
          else:
               for i in self:
                    if i == value:
                         return True
               return False

     def __iter__(self)-> Iterator[Any]:
          """
          used to iter through a linked list
          """
          return self.iter_forward()
     
     def _get_node(self,key: int)-> Node:
          """
          helper function use to get a node
          Args...
               key -> takes an integer value as key/index
          returns a key-1 node 
          Raises:
               IndexError:
                    if list is empty
                         or
                    if key is greater than the length of linked list     
          """
          if self.head is None:
               raise IndexError("list is empty")
          if key < 0:
               key += self._size
          if key >= self._size or key < 0:
               raise IndexError("index out of bound")
          if self.head is self.tail and key == 0:
               return self.head
          elif key == self._size - 1:
               return self.tail
          else:
               index = 1
               current = self.head
               while current :
                    if key == index:
                         return current
                    index += 1
                    current = current.next
     
     def iter_forward(self)-> Iterator[Any]:
          """
          Iterate over the linked list from head to tail.
          Yields:
               The value of each node.
          Raises:
               ValueError:
                    If the linked list is empty.
          """
          if self.head is None:
               raise IndexError("list is empty")
          else:
               current = self.head
               while current:
                    yield current.value
                    current = current.next

     def append(self,value: Any)-> None:
          """
          Appending the value to the last node of the doubly linked list
          Args... 
               value -> to append a value to the linked list 
          """
          newNode = Node(value)
          if self.head is None:
               self.head = newNode
               self.tail = newNode
          else:
               self.tail.next = newNode
               self.tail = newNode
          self._size += 1
     
     def remove(self,value: Any)-> bool:
               """
               use to remove an value from linked list
               Args...
                    value-> value to be deleted
               returns True if element is deleted/removed
               returns False if element is Not deleted/removed
               Raises:
                    IndexError:
                         if linked list is empty
               
               """
               if self.head is None:
                    raise IndexError("list is empty")
               if self.head is self.tail and self.head.value == value:
                    self.head = None
                    self.tail = None
                    self._size -= 1
                    return True
               if self.head.value == value:
                    self.head = self.head.next
                    self._size -= 1
                    return True
               else:
                    current = self.head
                    while current.next:
                         if current.next is self.tail:     
                              if self.tail.value == value:
                                   current.next = None
                                   self.tail = current
                                   self._size -= 1
                                   return True
                         elif current.next.value == value:
                              current.next = current.next.next
                              self._size -= 1
                              return True 
               return False
     
     def reverse(self)-> Iterator[Any]:
          """
          reverses the linked list mutates the whole linked list
          Yield...
               returns a value 
          Raises...
               IndexError:
                    if linked list is Empty
           
          """
          if self.head is None:
               raise IndexError("linked list is empty")
          if self.head is self.tail:
               yield self.head.value
               return
          else:
               self.tail = self.head
               previous = None
               current = self.head
               while current:
                    nextNode=current.next
                    current.next = previous
                    previous = current
                    current = nextNode
               self.head = previous

          newnode = self.head
          while newnode:
               yield newnode.value
               newnode = newnode.next
                         
     def clear(self)-> None:
          """
          clears all the linked list
          """
          self.head = None
          self.tail = None
          self._size = 0
                     
                              
                    