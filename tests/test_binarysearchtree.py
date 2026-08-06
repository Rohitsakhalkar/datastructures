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

def test_inorder():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bstlist = []
    for  i in bst:
        bstlist.append(i)
    assert bstlist == [10,20,30,50,60,70,80]

def test_postorder():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bstlist = []
    for  i in bst.postorder():
        bstlist.append(i)
    assert bstlist == [20,30,10,60,80,70,50]

def test_preorder():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bstlist = []
    for  i in bst.preorder():
        bstlist.append(i)
    assert bstlist == [50,10,30,20,70,60,80]

def test_min():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    assert bst.min() == 10

def test_max():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    assert bst.max() == 80

def test_bsf_traversal():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(10)
    bst.insert(30)
    bst.insert(20)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bstlist = []
    for i in bst.bfs_traversal():
        bstlist.append(i)
    assert bstlist == [50,10,70,30,60,80,20]