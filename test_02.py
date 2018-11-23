import requests
import pytest
import json


class TestClass:
    @classmethod
    def setup_class(cls):
        self.books_url = base_url + "/books"

    @classmethod
    def teardown_class(cls):
        pass

@pytest.fixture()
def book():
    return ' Book_01 '


@pytest.fixture(scope="session")
def base_url():
    return "http://pulse-rest-testing.herokuapp.com"


@pytest.fixture()
def book_data(base_url):
    b = {'title': 'Title1', 'author': 'New Author'}
    yield b
    requests.delete(base_url+"book/"+str(b["id"]))


@pytest.fixture()
def clean(base_url):
    yield
    # to do: clean all


with open("data_books.json", encoding="utf8") as f:
    books_data = json.load(f)


@pytest.mark.parametrize("book_data", books_data, ids=["...letter...", "...spec symbols.."])
def test_create_book(base_url, book_data, clean_book_ids):
    response = requests.post(books_url, data=book_data)
    assert response.status_code == 201
    response_body = response.json()
    assert "id" in response_body
    book_data["id"] = response_body["id"]
    assert book_data == response_body
    clean_book_ids.append(book_data["id"])


@pytest.mark.parametrize("book_data", books_data, ids=["...letter...", "...spec symbols.."])
def test_read_book(base_url, book_data, clean_book_ids):
    response = requests.get(books_url, data=book_data)
    assert response.status_code == 201
    response_body = response.json()
    assert "id" in response_body
    book_data["id"] = response_body["id"]
    assert book_data == response_body
    clean_book_ids.append(book_data["id"])


if __name__ == '__main__':
    pass
