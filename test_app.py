from app import hello

def test_hello():
    assert hello() == "Hello, Smart Inventory Agent!"

def test_dummy():
    assert 1 + 1 == 2