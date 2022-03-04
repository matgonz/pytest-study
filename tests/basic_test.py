import pytest

def test_first_method():
    val = 3 + 3
    assert val == 5

def not_foo_bar():
    pass

@pytest.mark.smoke
def test_with_marks():
    assert True