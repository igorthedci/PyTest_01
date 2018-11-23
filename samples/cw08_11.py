import pytest


@pytest.fixture
def fixt1():
    print("\n Initialization of fixture")
    fixture = "I am a fixture"
    return fixture


def test_1(fixt1):
    print(' - test_1()')
    assert fixt1


def test_2(fixt1):
    print(' - test_2()')
    assert 1 == 1
