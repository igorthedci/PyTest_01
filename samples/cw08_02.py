# для тестирования классов...
import pytest


@pytest.fixture()
def user():
    return User(name='Roman', age=30)


@pytest.fixture
def task(user):
    return Task(user=user, name='...')


def test_task(user, task):
    assert task.user.name == user.name

