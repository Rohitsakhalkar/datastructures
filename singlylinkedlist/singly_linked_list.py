from .node import Node 
from typing import Any, Iterator



class SinglyLinkedList:
     def __init__(self):
          self._size: int = 0
          self.head: Node | None = None
          self.tail: Node | None = None
     
     def __len__(self)-> int:
          return self._size
     
     def __str__(self)-> str:
          return f"[{" , ".join(str(value)for value in self)}]"
     
     def __repr__(self)-> str:
          return f"object: {self.__class__.__name__}({[ele for ele in self]})"

     def __bool__(self)-> bool:
          return self._size > 0
     
     def __eq__(self, other: Node)-> bool:
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
          return self.iter_forward()
     
     def _get_node(self,key: int)-> Node:
          # returns the previous node that you want
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
          if self.head is None:
               raise IndexError("list is empty")
          else:
               current = self.head
               while current:
                    yield current.value
                    current = current.next

     def append(self,value: Any)-> None:
          newNode = Node(value)
          if self.head is None:
               self.head = newNode
               self.tail = newNode
          else:
               self.tail.next = newNode
               self.tail = newNode
          self._size += 1
     
     def remove(self,value: Any)-> bool:
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
          self.head = None
          self.tail = None
          self._size = 0
                     
                              
                    