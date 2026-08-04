from queue import Queue

def test_enqueue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    assert len(q) == 2

def test_len():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.dequeue()
    assert len(q) == 2

def test_dequeue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.dequeue() == 10

def test_str():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert str(q) == "[10,20,30]"

def test_is_empty():
    q = Queue()
    q.enqueue(10)
    assert q.is_empty() == False

def test_is_full():
    q = Queue()
    q._max = 3
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.is_full()

def test_front():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert  q.front() == 10

def test_rear():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert  q.rear() == 30

def test_clear():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.clear()
    assert len(q) == 0

def test_bool():
    q = Queue()
    q.enqueue(10) 
    assert True if q else False