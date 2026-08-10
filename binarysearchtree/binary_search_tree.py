# Built by Sakhalkar, in search of meaning.
from .node import Node
from typing import Any, Iterator

class BinarySearchTree:

    def __init__(self)-> None:
        self.root = None
        self._size = 0

    def __iter__(self)-> Iterator[Any]:
        """
        Iterates over the binary search tree in Inorder
        """
        return self.inorder()

    def __len__(self)-> int:
        """
        returns the number of element present in the binary tree
        """
        return self._size

    def __str__(self)-> str:
        """
        returns a string of values in Inorder traversal
        """
        return f"[{",".join(str(value) for value in self)}]"

    def __repr__(self)-> str:
        """
        returns a string of values in Indorder traversal
        """
        return f"Binary Search Tree(Inorder value:[{",".join(str(value) for value in self)}])"

    def __contains__(self, value: int)-> bool:
        """
        returns a true if value is present in the binary search tree
        Args...
            value-> the value to be searched
        """
        return self.search(value)

    def min(self)-> int:
        """
        returns the minium value that is present in the binary search tree
        Raises...
            IndexError:
                if binary tree is empty
        """
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._min(self.root)
    
    def _min(self, node: Node)-> int:
        """
        hepler recursive function that searches for the left most node to get the minimum value
        Args...
            node-> the left node to visit 
        """
        if node.left is None:
            return node.value
        return self._min(node.left)

    def max(self)-> int:
        """
        returns the maximum value that is present in the binary search tree
        Raises...
            IndexError:
                if binary tree is empty
        """

        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._max(self.root)

    def _max(self,node: Node)-> int:
        """
        hepler recursive function that searches for the righh most node to get the maximum value
        Args...
            node-> the left node to visit 
        """
        if node.right is None:
            return node.value
        return self._max(node.right)

    def height(self)-> int:
        """
        return the height of the binary tree (number of edges not nodes)
        """
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._height(self.root)

    def _height(self, node: Node)-> int:
        """
        helper recursive function to find the height of the binary tree
        Args...
            node-> the node that need to be visited 
        """
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height,right_height)

        

    def search(self, value: int)-> bool:
        """
        returns bool value True if value is present or False  
        Args...
            value-> the value to be searched 
        Raises...
            IndexError:
                if binary tree is empty
        """
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._search(self.root,value)
        
    def _search(self, node: Node, value: int)-> bool:
        """
        helper function to find if a value exist in binary search tree
        Args...
            node-> the node that to be visited 
            value-> the value to be searched
        """
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
           return self._search(node.left,value)
        elif value >= node.value:
           return self._search(node.right,value)
        

    def inorder(self)-> Iterator[Any]:
        """
        Iterates over the binary tree and returns the values in Inorder traversal
        Raises...
            IndexError:
                if binary tree is empty
        """
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._inorder(self.root)
    
    def _inorder(self, node: Node)-> Iterator[Any]:
        """
        helper function Iterates over the binary tree and returns the values in Inorder traversal
        Args...
            node-> the node that need to visited
        """
        if node is None:
            return
        yield from self._inorder(node.left)
        yield node.value
        yield from self._inorder(node.right)

    def postorder(self)-> Iterator[Any]:
        """
        Iterates over the binary tree and returns the values in postorder traversal
            Raises...
                IndexError:
                    if binary tree is empty
        """
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._postorder(self.root)

    def _postorder(self, node: Node)->Iterator[Any]:
        """
        helper function Iterates over the binary tree and returns the values in postorder traversal
        Args...
            node-> the node that need to visited
        """
        if node is None:
            return
        yield from self._postorder(node.left)
        yield from self._postorder(node.right)
        yield node.value

    def preorder(self)-> Iterator[Any]:
        """
        Iterates over the binary tree and returns the values in preorder traversal
        Raises...
            IndexError:
                if binary tree is empty
        """
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._preorder(self.root)

    def _preorder(self,node: Node)-> Iterator[Any]:
        """
        helper function Iterates over the binary tree and returns the values in preorder traversal
        Args...
            node-> the node that need to visited
        """
        if node is None:
            return 
        yield node.value
        yield from self._preorder(node.left)
        yield from self._preorder(node.right)

    def insert(self,value: int)->None:
        """
        inserts a value in the binary tree 
        Args...
            value-> the value to be inserted 
        """
        if not self.root:
            self.root = Node(value)
            self._size += 1
            return
        self._insert_node(self.root,value)

    def _insert_node(self,node: Node,value: int)-> None:
        """
        helper function inserts a value in binary tree 
        Args...
            node-> the node to be visited 
            value-> the value to be visited
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                self._size += 1 
                return
            self._insert_node(node.left , value)

        if value >= node.value:
            if node.right is None:
                node.right = Node(value)
                self._size += 1
                return
            self._insert_node(node.right, value)
        

    
    def delete(self, value: int)-> bool:
            """
            returns a bool True if value is Deleted from the tree
            Args...
                value-> value to be deleted
            Raises...
                IndexError:
                    if the binary tree is empty
            """
            if self.root is None:
                raise IndexError("binary tree is empty")
            parent = None
            result = self._delete_node(self.root,parent,value)
            if result is None:
                return False
            parent , child = result
            if child.left is None or child.right is None:
                replacement = child.left or child.right
                self._replace_child(parent,child,replacement)
                self._size -= 1
                return True
            elif child.left and child.right:
                successor_parent, successor = self._find_successor(child.right,child)
                child.value = successor.value
                self._replace_child(successor_parent,successor,successor.right)
                self._size -= 1
                return True
            return False
    
    def _replace_child(self, parent: Node, child: Node, replacement: Node)-> None:
        """
        helper function use to assign and replace child node with grand parent node when a node gets deleted
        Args...
            parent-> the parent of the node the is to be deleted
            child-> the node that is to be deleted
            replacement-> the node which is the replacement for child node
        """
        if parent.left is child:
            parent.left = replacement
        else :
            parent.right = replacement

    def _find_successor(self, node: Node , parent: Node | None = None)-> tuple[Node, Node]:
        """
        helper function to find a successor for a node which has two child nodes 
        returns parent and successor 
        Args...
            node-> the current node or the node to visit
            parent-> the parent node

        """
        if node.left:
            parent = node
            return self._find_successor(node.left,parent)
        return parent, node
        
    def _delete_node(self, node: Node, parent: Node, value: Node)-> tuple[Node, Node]:
        """
        helper function to find the node to be deleted and the parent node
        returns a parent and child node
        Args...
            node-> the node to visit
            parent-> the parent of the current node
            value-> the value to be searched
        """
        if node is None:
            return
        if value < node.value:
            parent = node
            return self._delete_node(node.left,parent,value)
        elif value > node.value:
            parent = node
            return self._delete_node(node.right,parent,value)
        else:
            return parent, node

    def clear(self)-> None:
        """
        clears the binary tree
        """
        self.root = None
        self._size = 0

    def is_empty(self)-> bool:
        """
        returns a bool True if the binary tree is empty or False
        """
        return True if self.root else False

    def bfs_traversal(self)-> Iterator[Any]:
        """
        returns the values in bfs(breadth first search) order 
        Raises...
            IndexError:
                if binary search tree is empty
        """
        if self.root is None:
            raise IndexError("Binary search tree is empty")
        queue = []
        queue.append(self.root)
        while queue:
            front = queue.pop(0)
            yield front.value
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)