from .node import Node
from typing import Any

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self._size = 0

    def __iter__(self):
        return self.inorder()

    def __len__(self):
        return self._size

    def __str__(self):
        return f"[{",".join(str(value) for value in self)}]"

    def __repr__(self):
        return f"Binary Search Tree(Inorder value:[{",".join(str(value) for value in self)}])"

    def __contains__(self, value):
        return self.search(value)

    def min(self):
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._min(self.root)
    
    def _min(self,node):
        if node.left is None:
            return node.value
        return self._min(node.left)

    def max(self):
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._max(self.root)

    def _max(self,node):
        if node.right is None:
            return node.value
        return self._max(node.right)

    def height(self):
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._height(self.root)

    def _height(self,node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height,right_height)

        

    def search(self,value):
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._search(self.root,value)
        
    def _search(self,node,value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
           return self._search(node.left,value)
        elif value >= node.value:
           return self._search(node.right,value)
        

    def inorder(self):
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._inorder(self.root)
    
    def _inorder(self, node):
        if node is None:
            return
        yield from self._inorder(node.left)
        yield node.value
        yield from self._inorder(node.right)

    def postorder(self):
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return
        yield from self._postorder(node.left)
        yield from self._postorder(node.right)
        yield node.value

    def preorder(self):
        if self.root is None:
            raise IndexError("binary search tree is empty")
        return self._preorder(self.root)

    def _preorder(self,node):
        if node is None:
            return 
        yield node.value
        yield from self._preorder(node.left)
        yield from self._preorder(node.right)

    def insert(self,value):
        if not self.root:
            self.root = Node(value)
            self._size += 1
            return
        self._insert_node(self.root,value)

    def _insert_node(self,node,value):
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
        

    
    def delete(self,value):
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
    
    def _replace_child(self,parent,child,replacement):
        if parent.left is child:
            parent.left = replacement
        else :
            parent.right = replacement

    def _find_successor(self,node,parent = None):
        if node.left:
            parent = node
            return self._find_successor(node.left,parent)
        return parent, node
        
    def _delete_node(self,node,parent,value):
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

    def clear(self):
        self.root = None
        self._size = 0

    def is_empty(self):
        return True if self.root else False

    def bfs_traversal(self):
        queue = []
        queue.append(self.root)
        while queue:
            front = queue.pop(0)
            yield front.value
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
            
        



           

       