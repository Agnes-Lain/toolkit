from toolkit.lib import factorial, collatz

def test_factorial():
    assert factorial(4) == 24

def test_factorial_one():
    assert factorial(1) == 1

def test_collatz_even():
    assert collatz(4) == 2

def test_collatz_odd():
    assert collatz(5) == 16
