import pytest
# from fixtures import book


@pytest.mark.skip(reason=" no book")
def test_01(book):
    print("  I'm test   ")
    a = 100
    assert a == book


def test_02():
    print("   I'm test   ")
    a = 100
    assert a == 100
