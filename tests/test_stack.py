from stack import Stack

def test_push():
    s = Stack()
    s.push(10)
    s.push(20)
    assert len(s) == 2

def test_pop():
    s = Stack()
    s.push(10)
    s.push(30)
    s.pop()
    assert len(s) == 1

def test_peek():
    s = Stack()
    s.push(10)
    s.push(20)
    assert s.peek() == 20

def test_isempty():
    s = Stack()
    assert s.is_empty() == True

def test_isfull():
    s = Stack()
    s._max = 3
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.is_full() == True

def test_len():
    s = Stack()
    s.push(10)
    assert len(s) == 1

def test_str():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    assert str(s) == "[30,20,10]"

