from addition import add

def test_add_positive():
    assert add(10, 20) == 30

def test_add_negative():
    assert add(-5, 5) == 0

def test_add_zeros():
    assert add(0, 0) == 0
