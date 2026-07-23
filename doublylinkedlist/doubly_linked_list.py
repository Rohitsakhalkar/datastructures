from .node import Node
from typing import Any , Iterator


class DoublyLinkedList:

   def __init__(self) -> None:
      self._size: int = 0
      self.head: Node | None = None
      self.tail: Node | None = None
   
   def __len__(self) -> int:
       """
        returns the length of Linked list

       """
       return self._size  

   def __iter__(self) -> Iterator[Any]:
       """
         used to iter through a linked list
         
       """
       return self.iter_forward() 
   
   def __reversed__(self) -> Iterator[Any]:
       """
         used to iter in reverse through a linked list

       """
       return self.iter_backward()
   
   def __contains__(self, value: Any)-> bool:
       """
       checks if value is present in the list or not

         Args...
            value -> takes a value to check if its present

         returns true if present
         returns false if not present

         Raises:
            indexError:
               If the linked list is empty.
       """
       return self.search(value)

   def __str__(self)-> str:
       """
        used to print the value 

        returns a string

       """
       return f"[{" , ".join(str(value) for value in self)}]" 
   
   def __repr__(self)-> str:
      """
         used to print object/linked list detail in debugger 

         returns a string

      """
      return f"object:{self.__class__.__name__}({[element for element in self]})"
   
   def __eq__(self, other: Node) -> bool:
      """
         used to check if two object are equal

         Args...
            other -> another object

         returns true if both linked list are same or have same values
         returns false if both linked list is not same or don't have same values

         Raises:
            indexError:
               If linked list is empty
      """
      if self.head is None:
         raise IndexError("Linked list is Empty")
      if self is other :
         return True
      if self._size == len(other):
         current = self.head
         for i in other:
            if i != current.value:
               return False
            current=current.next
         return True
      else:
         return False

   def __bool__(self)-> bool:
      """
         bool returns true if object/linked list has values in it 
         returns false if object/linked list has no values in it
      """
      return self._size > 0

   def __getitem__(self, key: int)-> Any:
      """
      used to get an element from list by a key
         Args...
            key -> takes a integer value index 
         returns the value of the index
         Raises:
            indexError:
               If linked list is empty or the key is greater then the actual linked list
      """
      return self._get_node(key).value  
   
   def __delitem__(self, key: int) -> None:
      if self.head is None:
         raise IndexError("out of bound")
      if key < 0:
         key += self._size
      if key >= self._size or key < 0:
         raise IndexError("index out of bound")
      if self.head is self.tail:
          self.head = None
          self.tail = None
      elif key == 0:
         self.head = self.head.next
         self.head.previous = None
      elif key == self._size - 1:
         self.tail=self.tail.previous
         self.tail.next=None
      else:
         current=self._get_node(key)
         current.previous.next=current.next
         current.next.previous=current.previous
      self._size -= 1
   
   def __setitem__(self, key: int, value: Any)-> None:
      """
      used to replace an element in the list 

      Args...
         key -> index the value to be added to
         value -> the value that should be added
      
      Raises:
         IndexError:
            if linked list is empty and the key is not 0
                     or
            if key is greater then the size of linked list

      """
      newNode = Node(value)
      if self.head is None:
          if key != 0:
            raise IndexError("index out of bound")
          self.head = newNode
          self.tail = newNode
      if key < 0:
         key += self._size
      if key > self._size or key < 0:
         raise IndexError("index out of bound")
      if self.head is self.tail:
         self.head=newNode
         self.tail=newNode
      elif key == 0 :
          newNode.next = self.head.next
          self.head.next.previous = newNode
          self.head = newNode
      elif key == self._size - 1:
          newNode.previous = self.tail.previous
          self.tail.previous.next = newNode
          self.tail = newNode
      else:
          current = self._get_node(key)
          newNode.next = current.next
          newNode.previous = current.previous
          current.previous.next = newNode
          current.next.previous = newNode
       

   def _get_node(self, key: int)-> Node:
      """
         helper function use to get a node

         Args...
            key -> takes an integer value as key/index
         
         returns a node affiliated to the key

         Raises:
            IndexError:
               if list is empty
                     or
               if key is greater then the size of the linked list
      """
      mid= self._size // 2
      if self.head is None:
          raise IndexError("Index out of bound")
      if key < 0:
         key += self._size
      if key >= self._size or key < 0:
         raise IndexError("index out of bound")
      if key < mid:
         index = 0
         current = self.head
         while index < key:
            index += 1
            current=current.next
         return current
      else:
         index = self._size - 1
         current=self.tail
         while index > key :
            index -= 1
            current=current.previous
         return current 

   def search(self, value: Any)-> bool:
       """
         searches for an element in the linked list

         Args...
            value -> the value to be searched
         
         returns true if value is present
         returns false if value is not present

         Raises:
            IndexError:
               if linked list is empty
       """
       if self.head is None:
          raise IndexError("Linked list is empty")
       current = self.head
       while current:
           if current.value == value:
               return True
           current = current.next
       return False
   
   def insert(self, key: int, value: Any) -> None:
      """
      inserts a value in the linked list on the index provided

      Args...
         key -> takes a key/index 
         value -> takes the value to add at the key/index
      
      Raises:
         IndexError:
            if list is empty and the key provided is not 0 
                              or
            if the key is greater then the size of the linked list
      """
      newNode = Node(value)
      if self.head is None:
          if key != 0:
            raise IndexError("index out of bound")
          self.head = newNode
          self.tail = newNode
      if key < 0:
         key += self._size
      if key >= self._size or key < 0:
         raise IndexError("index out of bound")
      elif key == 0 :
          newNode.next = self.head
          self.head.previous = newNode
          self.head = newNode
      elif key == self._size :
          newNode.previous = self.tail
          self.tail.next = newNode
          self.tail = newNode
      else:
          current = self._get_node(key)
          newNode.next = current
          newNode.previous = current.previous
          current.previous.next = newNode
          current.previous = newNode
      self._size += 1  


   def append(self, value: Any) -> None:
      '''
         Appending the value to the last node of the doubly linked list

      Args... 
          value -> to append a value to the linked list 

      '''
      current = Node(value)
      if  self.head is None:
         self.head = current
         self.tail = current
      else:
         self.tail.next = current
         current.previous = self.tail
         self.tail =  current
      self._size += 1
      
   def prepend(self, value: Any)-> None:
       current = Node(value)
       if self.head is None:
           self.head = current
           self.tail = current
       else:
           self.head.previous = current
           current.next = self.head
           self.head = current
       self._size += 1

   def iter_forward(self) -> Iterator[Any]:
      """
         Iterate over the linked list from head to tail.

         Yields:
            The value of each node.

         Raises:
            ValueError:
               If the linked list is empty.

      """
      if  self.head is None:
          raise ValueError("Linked List is empty")
      current = self.head
      while current:
         yield current.value
         current = current.next

   def iter_backward(self) -> Iterator[Any]:
      """
         Iterate over the linked list from tail to head.

         Yields:
            The value of each node.

         Raises:
            ValueError:
               If the linked list is empty.

      """
      if self.head is None:
         raise ValueError("Linked List is empty")
      current = self.tail
      while current:
         yield current.value
         current = current.previous

   def remove(self, value: Any) -> bool:
      '''
         use to remove an value from linked list

         Args...
            value-> value to be deleted
         returns True if element is deleted/removed
         returns False if element is Not deleted/removed

         Raises:
            IndexError:
               if linked list is empty

      '''
      if  self.head is None:
         raise IndexError("linked is empty")
      
      if self.head is self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self._size -= 1
            return True
      elif self.head.value == value:
            self.head = self.head.next
            self.head.previous = None
            self._size -= 1
            return True
      elif self.tail.value == value:
            self.tail = self.tail.previous
            self.tail.next = None
            self._size -= 1
            return True
      current = self.head.next
      while current is not self.tail:
         if current.value == value:
            current.previous.next = current.next
            current.next.previous = current.previous
            self._size -= 1
            return True
         current = current.next
      return False

   def clear(self) -> None:
       """

       clears the all the linked list value 

       """
       self.head = None
       self.tail = None
       self._size = 0
