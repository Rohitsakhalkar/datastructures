from singlylinkedlist import SinglyLinkedList

def test_append():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    assert len(sll) == 2

def test_remove():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    assert sll.remove(10)

def test_len():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    assert len(sll) == 3

def test_str():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    assert str(sll) == "[10 , 20]"

def test_bool():
    sll = SinglyLinkedList()
    sll.append(10)
    assert  True if sll else False

def test_eq():
    sll = SinglyLinkedList()
    sll2 = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll2.append(10)
    sll2.append(20) 
    assert sll == sll2

def test_reversed():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    rev = reversed(sll)
    revlist = [str(i) for i in rev]
    assert revlist == ['20', '10']

def test_getitem():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    assert sll[1] == 20

def test_setitem():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll[2] = 40
    assert sll[2] == 40

def test_delitem():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    del sll[1]
    assert len(sll) == 1

def test_contains():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    assert 10 in sll

def test_clear():
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.clear()
    assert len(sll) == 0