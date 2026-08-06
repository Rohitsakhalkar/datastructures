from doublylinkedlist import DoublyLinkedList
from singlylinkedlist import SinglyLinkedList
from binarysearchtree import BinarySearchTree
 #dll=DoublyLinkedList()
# sll = SinglyLinkedList()
# sll.append(10)
# sll.remove(10)
# sll.append(20)
# sll.append(30)
# sll.append(10)
# sll.append(40)
# print(sll[-2])
# del sll[-2]
# if 10 in sll:
#     print("yes")
# print(len(sll))
# sll[0]=10
# print(sll)

# dll = DoublyLinkedList()
# dll.append(10)
# dll.append(20)
# print(dll)

bst = BinarySearchTree()
bst.insert(50)
bst.insert(10)
bst.insert(30)
bst.insert(20)
bst.insert(70)
bst.insert(80)
bst.insert(60)
print("inorder",end=":")
for i in bst.inorder():
    print(i,end=" ")
print("\npostorder",end=":")
for i in bst.postorder():
    print(i,end=" ")
print("\npreorder",end=":")
for i in bst.preorder():
    print(i,end=" ")
print("\n",bst)
for i in bst.bfs_traversal():
    print(i)