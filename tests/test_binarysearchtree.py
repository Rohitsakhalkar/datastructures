from binarysearchtree import BinarySearchTree

def test_insert():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    assert len(bst) == 5

def test_search():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(20)
    bst.insert(60)
    assert bst.search(60) 

def test_delete():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    bst.delete(50)
    assert len(bst) == 4

def test_height():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(20)
    bst.insert(10)
    assert bst.height() == 2

def test_len():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    assert len(bst) == 5