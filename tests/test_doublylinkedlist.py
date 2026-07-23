from doublylinkedlist import DoublyLinkedList

def test_append():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    assert len(dll) == 2

def test_remove():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.remove(20)
    assert len(dll) == 1

def test_len():
    dll = DoublyLinkedList()
    dll.append("helllo")
    dll.append("world")
    assert len(dll) == 2

def test_str():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    assert str(dll) == "[10 , 20 , 30]"

def test_search():
    dll = DoublyLinkedList()
    dll.append(30)
    dll.append(40)
    assert 40 in dll

def test_eq():
    dll1 = DoublyLinkedList()
    dll2 = DoublyLinkedList()
    dll1.append(10)
    dll2.append(10)
    assert dll1 == dll2

def test_insert():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.insert(1,30)
    assert 30 in dll

def test_setitem():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll[1] = 30
    assert dll[1] == 30

def test_prepend():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.prepend(30)
    assert dll[0] == 30

def test_clear():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.clear()
    assert len(dll) == 0

def test_len():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    assert len(dll) == 2

def test_get_item():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    assert dll[1] == 20

def test_del_item():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    del dll[1]
    assert  len(dll) == 1
    